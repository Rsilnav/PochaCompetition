from DummyPlayer import *
from Card import *
from Deck import *
import copy

'''
def playRound(players, deck, dealtCardsPerPlayer, firstPlayer):
	# Correction check
	dealtCardsNumber = len(players) * dealtCardsPerPlayer
	if dealtCardsNumber > 40:
		raise Exception

	# Deal cards
	if(dealtCardsNumber < 40):
		trumpCard = deck.cards[dealtCardsNumber]
	else:
		trumpCard = deck.cards[39]
	dealtCards = [[] for i in xrange(len(players))]
	for i in xrange(len(players)):
		pId = (i+firstPlayer) % len(players)
		dealtCards[pId] = deck.cards[i*dealtCardsPerPlayer:(i+1)*dealtCardsPerPlayer]
		players[pId].setInitialHand(dealtCards[pId])
		if(dealtCardsNumber < 40):
			players[pId].setTrump(trumpCard)
		else:
			players[pId].setTrump(trumpCard)

	# Ask for the bets:
	order = []
	bets = [0 for i in xrange(len(players))]
	bazas = [0 for i in xrange(len(players))]
	previousBets = []
	for i in xrange(len(players)):
		order.append((i+firstPlayer) % len(players))
		bet = players[order[i]].getBet(previousBets)
		bets[order[i]] = bet
		previousBets.append(bet)

	# Play each round as follows:
	lastWinner = firstPlayer
	for i in xrange(dealtCardsPerPlayer):
		order = []
		for i in xrange(len(players)):
			order.append((i+lastWinner) % len(players))
		playedCards = []
		for i in order:
			playedCards.append(players[order[i]].getCard(playedCards, order))
			# We should check here that the player has that card and is a suitable card.
		lastWinner = winnerCard(trumpCard, playedCards)
		bazas[order[lastWinner]] += 1
	
	# Compare bets with won turns and get points of this round
	points = []
	for i in xrange(len(players)):
		if bets[i] == bazas[i]:
			points.append(10+5*bets[i])
		else:
			points.append(-5*abs(bets[i]-bazas[i]))
	return points

def playStaticGame(cardsPerRound = 10, rounds = 20):
	inititalDeck = Deck()
	#inititalDeck.shuffle()

	player1 = DummyPlayer(4,0)
	player2 = DummyPlayer(4,1)
	player3 = DummyPlayer(4,2)
	player4 = DummyPlayer(4,3)

	points = [0, 0, 0, 0]
	players = [player1, player2, player3, player4]
	for round in xrange(rounds):
		deck = inititalDeck
		newPoints = playRound(players, deck, cardsPerRound, round)
		#newPoints = playRound(players, deck, round +1, round)
		points = map(sum, zip(points, newPoints))
		#print points
'''


def playGame(numeroDePartidas, tipoDePartida, cantidadDeRondas, tipoCambiaMano, barajarEntreRondas, numeroDeBazas, jugadores, jugadorPrimero):
	
	# Crea la baraja inicial en caso de que sean partidas estaticas
	if barajarEntreRondas == 0:
		barajaInicial = Deck()

	# Informa a todo el mundo de los jugadores que hay
	for jugador in jugadores:
		jugador.setTotalPlayers(len(jugadores))

	# Para cada partida
	for partida in xrange(numeroDePartidas):

		# Crea las puntuaciones iniciales
		puntuaciones = []
		for i in xrange(len(jugadores)):
			puntuaciones.append(0)

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
				numeroDeBazas = 40/len(jugadores)

			# Repartir las cartas
			for jugador in xrange(len(jugadores)):
				jugadores[jugador].setInitialHand(baraja.cards[jugador*numeroDeBazas:(jugador+1)*numeroDeBazas])

			# Calcular el pinte
			if numeroDeBazas*len(jugadores) == 40:
				pinte = 39
			else:
				pinte = numeroDeBazas*len(jugadores)

			# Informar del pinte
			for jugador in jugadores:
				jugador.setTrump(baraja.cards[pinte])

			bets = []
			# Hacer apuestas
			for offset in xrange(len(jugadores)):
				jugadores[(offset+jugadorPrimero)%len(jugadores)].giveBets(bets)
				newBet = jugadores[(offset+jugadorPrimero)%len(jugadores)].getBet()
				print "El jugador", (offset+jugadorPrimero)%len(jugadores), "hace la apuesta", newBet
				bets.append(newBet)

			# Para cada baza de la que se compone cada ronda
			ganadorBaza = primero
			for baza in xrange(numeroDeBazas):
				
				for carteo in xrange(len(jugadores)):
					pass

					# TODO: Echar carta

				# Calcular ganador de la baza

				# Informar del ganador a todo el mundo
				# El ganador pasa a ser el primero




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

def winnerCard(trumpCard, playedCards):
	cards = len(playedCards)
	winner = 0
	for i in xrange(1,cards):
		if playedCards[i].getSuit() == playedCards[winner].getSuit():
			if playedCards[i].getNumber() > playedCards[winner].getNumber():
				winner = i
		elif playedCards[winner].getSuit() != trumpCard.getSuit():
			if playedCards[i].getSuit() == trumpCard.getSuit():
				winner = i
	return winner