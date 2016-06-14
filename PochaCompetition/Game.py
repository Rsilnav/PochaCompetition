from DummyPlayer import *
from Card import *
from Deck import *
import copy

# Dada una lista de cartas que han sido lanzadas en ese orden y una carta de pinte, devuelve la posicion
# de la carta dentro de la lista que resulta ganadora con las reglas de la pocha.
def cartaGanadora(cartaDePinte, cartasJugadas):
	cartas = len(cartasJugadas)
	ganador = 0
	for i in xrange(1,cartas):
		if cartasJugadas[i].getSuit() == cartasJugadas[ganador].getSuit():
			if cartasJugadas[i].getNumber() > cartasJugadas[ganador].getNumber():
				ganador = i
		elif cartasJugadas[ganador].getSuit() != cartaDePinte.getSuit():
			if cartasJugadas[i].getSuit() == cartaDePinte.getSuit():
				ganador = i
	return ganador

# Dada una carta de pinte, una lista de cartas jugadas y la mano del ultimo jugador que lanzo carta, comprueba
# que dicho jugador no haya efectuado un incumplimiento de las normas.
def comprobarCarta(cartaDePinte, cartasJugadas, manoJugador):
	cartas = len(cartasJugadas)
	if cartasJugadas[-1] not in manoJugador:
		return False
	if cartas == 1:
		return True
	else:
		cartaInicial = cartasJugadas[0]
		cartaJugada = cartasJugadas[-1]
		cartaGanadoraActual = cartasJugadas[cartaGanadora(cartaDePinte,cartasJugadas[:-1])]

		# Se ha roto la ronda ( carta ganadora es del palo del pinte, pero no se salio por pinte)
		if cartaInicial.getSuit() != cartaDePinte.getSuit() and cartaGanadoraActual.getSuit() == cartaDePinte.getSuit():
			# Sigue el palo del pinte (o de la carta ganadora actual)
			if cartaJugada.getSuit() == cartaDePinte.getSuit():
				#Comprobamos primero que no tenga cartas del palo de salida:
				for carta in manoJugador:
					if carta.getSuit() == cartaInicial.getSuit():
						return False
				if cartaJugada.getNumber() > cartaGanadoraActual.getNumber():
					return True
				else:
					# Comprobamos que no tenga en su mano una carta mas alta de pinte a la ganadora:
					for carta in manoJugador:
						if carta.getSuit() == cartaGanadoraActual.getSuit() and carta.getNumber() > cartaGanadoraActual.getNumber():
							return False
					return True
			# No sigue el palo de pinte ( o de la carta ganadora actual)
			else:
				# Tira una carta del palo inicial
				if cartaJugada.getSuit() == cartaInicial.getSuit():
					return True
				# No tira una carta del palo del pinte ni del inicial
				else:
					# Comprobamos que no tenga cartas del palo de salida, en cuyo caso seria trampa
					# Comprobamos que no tengas cartas del palo de pinte por encima a la carta ganadora actual.
					for carta in manoJugador:
						if carta.getSuit() == cartaInicial.getSuit():
							return False
						if carta.getSuit() == cartaGanadoraActual.getSuit() and carta.getNumber() > cartaGanadoraActual.getNumber():
							return False
					return True

		# No se ha roto la ronda
		else:
			if cartaJugada.getSuit() == cartaInicial.getSuit():
				if cartaJugada.getNumber() > cartaGanadoraActual.getNumber():
					return True
				else:
					# Comprobamos que no tenga cartas mas altas del palo inicial
					for carta in manoJugador:
						if carta.getSuit() == cartaInicial.getSuit() and carta.getNumber() > cartaGanadoraActual.getNumber():
							return False
			else:
				#Comprobamos que no tiene cartas del palo inicial
				for carta in manoJugador:
					if carta.getSuit() == cartaInicial.getSuit():
						return False
				if cartaJugada.getSuit() == cartaDePinte.getSuit():
					return True
				else:
					# Llegados a este punto no tiro ni del palo inicial ni del palo de pinte, comprobamos que no tenga cartas de pinte
					for carta in manoJugador:
						if carta.getSuit() == cartaDePinte.getSuit():
							return False

def playGame(numeroDePartidas, tipoDePartida, cantidadDeRondas, tipoCambiaMano, barajarEntreRondas, numeroDeBazas, jugadores, jugadorPrimero):
	
	numeroDeJugadores = len(jugadores)
	# Crea la baraja inicial en caso de que sean partidas estaticas
	if barajarEntreRondas == 0:
		barajaInicial = Deck()

	# Informa a todo el mundo de los jugadores que hay
	for jugador in jugadores:
		jugador.setTotalPlayers(numeroDeJugadores)

	# Para cada partida
	for partida in xrange(numeroDePartidas):

		# Crea las puntuaciones iniciales
		puntuaciones = [0 for i in xrange(numeroDeJugadores)]

		# Se crea la baraja que se usara en la partida
		if barajarEntreRondas == 0:
			baraja = copy.deepcopy(barajaInicial)
		elif barajarEntreRondas == 1:
			baraja = Deck()
			baraja.shuffle()

		primero = jugadorPrimero

		# Para cada ronda de la partida
		for ronda in xrange(cantidadDeRondas):

			# Calcular cartas si se pretenden repartir las maximas posibles
			if numeroDeBazas == 0:
				numeroDeBazas = 40/numeroDeJugadores

			# Repartir las cartas
			manoJugador = [[] for i in xrange(numeroDeJugadores)]
			for jugador in xrange(numeroDeJugadores):
				manoJugador[jugador] = baraja.cards[jugador*numeroDeBazas:(jugador+1)*numeroDeBazas]
				jugadores[jugador].setInitialHand(manoJugador[jugador])

			# Calcular el pinte
			if numeroDeBazas*numeroDeJugadores == 40:
				pinte = baraja.cards[39]
			else:
				pinte = baraja.cards[numeroDeBazas*numeroDeJugadores]

			# Informar del pinte
			for jugador in jugadores:
				jugador.setTrump(pinte)


			# Hacer apuestas
			bets = []
			apuestas = [0 for i in xrange(numeroDeJugadores)]
			for offset in xrange(numeroDeJugadores):
				idJugador = (offset+jugadorPrimero)%numeroDeJugadores
				jugadores[idJugador].giveBets(bets)
				newBet = jugadores[idJugador].getBet()
				#print "El jugador", idJugador, "hace la apuesta", newBet
				bets.append(newBet)
				apuestas[idJugador] = newBet

			# Para cada baza de la que se compone cada ronda
			ganadorBaza = primero
			bazas = [0 for i in xrange(numeroDeJugadores)]
			for baza in xrange(numeroDeBazas):
				# Calculamos el orden en que los jugadores lanzan sus cartas
				orden = []
				for i in xrange(numeroDeJugadores):
					orden.append((i+ganadorBaza) % numeroDeJugadores)
				cartasJugadas = []
				# Solicitamos una carta a cada jugador, informando de que cartas han echado el resto de jugadores.
				for idJugador in orden:
					cartasJugadas.append( jugadores[idJugador].getCard(cartasJugadas, orden) )
					if comprobarCarta(pinte, cartasJugadas, manoJugador[idJugador])== True:
						manoJugador[idJugador].remove(cartasJugadas[-1])
				# TO DO:
				# Informar de las cartas jugadas por todos los jugadores y el ganador de la baza.
				ganadorBaza = orden[cartaGanadora(pinte, cartasJugadas)]
				bazas[ganadorBaza] += 1

			for i in xrange(numeroDeJugadores):
				if apuestas[i] == bazas[i]:
					puntuaciones[i] += (10+5*apuestas[i])
				else:
					puntuaciones[i] += -5*abs(apuestas[i]-bazas[i])

			if tipoCambiaMano == 2:
				primero = (primero+1)%len(jugadores)

		if tipoCambiaMano == 1:
			primero = (primero+1)%len(jugadores)


		# Imprime las puntuaciones finales de cada partida
		print puntuaciones

def main():
	'''
	playStaticGame(1,10)
	'''

	numeroDePartidas = 1

	# 0 para partida a puntos
	# 1 para partida a rondas
	# POR EL MOMENTO SOLO HACER PARTIDAS A RONDAS
	tipoDePartida = 1

	cantidadDeRondas = 1

	# 0 para no cambiar de Mano
	# 1 para cambiar de Mano entre partidas
	# 2 para cambiar de Mano entre ronda
	tipoCambiaMano = 0

	# 0 para no barajar entre rondas
	# 1 para barajar entre rondas
	barajarEntreRondas = 0

	# Instanciar jugadores
	jugadores = []
	jugadores.append(DummyPlayer())
	jugadores.append(DummyPlayer())
	jugadores.append(DummyPlayer())
	jugadores.append(DummyPlayer())

	# numero de bazas por cada ronda
	# 0 si se quiere que sean las maximas posibles segun el numero de jugadores
	numeroDeBazas = 0

	# Jugador que empieza siendo el primero en pedir/jugar
	jugadorPrimero = 0

	playGame(numeroDePartidas, tipoDePartida, cantidadDeRondas, tipoCambiaMano, barajarEntreRondas, numeroDeBazas, jugadores, jugadorPrimero)



if __name__ == '__main__':
	main()