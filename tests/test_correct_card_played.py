import unittest
from PochaCompetition.Card import Card
from PochaCompetition.Game import comprobarCarta

class TestUM(unittest.TestCase):

	def setUp(self):
		pass

	def test_card_not_in_hand(self):
		# Una carta que no esta en su mano
		cartaDePinte = Card(0,0) # Dos de oros
		cartasJugadas = [Card(1,1), Card(2,2)]
		manoJugador = []
		result = comprobarCarta(cartaDePinte, cartasJugadas, manoJugador)
		self.assertEqual(result, False)

	def test_first_player(self):
		cartaDePinte = Card(0,0) # Dos de oros
		cartasJugadas = [Card(0,1)]
		manoJugador = [Card(0,1)]
		result = comprobarCarta(cartaDePinte, cartasJugadas, manoJugador)
		self.assertEqual(result, True)

	def test_second_player_follows(self):
		cartaDePinte = Card(0,0)		
		cartasJugadas = [Card(0,1), Card(1,1)]
		manoJugador = [Card(1,1)]
		result = comprobarCarta(cartaDePinte, cartasJugadas, manoJugador)
		self.assertEqual(result, True)

	def test_second_player_does_not_follow(self):
		cartaDePinte = Card(0,0)		
		cartasJugadas = [Card(0,1), Card(1,0)]
		manoJugador = [Card(1,0),Card(1,1)]
		result = comprobarCarta(cartaDePinte, cartasJugadas, manoJugador)
		self.assertEqual(result, False)

	def test_second_player_trump_bad(self):
		cartaDePinte = Card(0,0)		
		cartasJugadas = [Card(0,1), Card(1,2)]
		manoJugador = [Card(1,0),Card(1,2)]
		result = comprobarCarta(cartaDePinte, cartasJugadas, manoJugador)
		self.assertEqual(result, False)

	def test_third_player_follow_low(self):
		cartaDePinte = Card(0,0)
		cartasJugadas = [Card(3,1), Card(1,0), Card(1,1)]
		manoJugador = [Card(1,1), Card(6,1)]
		result = comprobarCarta(cartaDePinte, cartasJugadas, manoJugador)
		self.assertEqual(result, True)

	def test_third_player_follow_bad(self):
		cartaDePinte = Card(0,0)
		cartasJugadas = [Card(3,1), Card(5,1), Card(1,1)]
		manoJugador = [Card(1,1), Card(6,1)]
		result = comprobarCarta(cartaDePinte, cartasJugadas, manoJugador)
		self.assertEqual(result, False)

	def test_third_player_follow_good(self):
		cartaDePinte = Card(0,0)
		cartasJugadas = [Card(3,1), Card(5,1), Card(6,1)]
		manoJugador = [Card(1,1), Card(6,1)]
		result = comprobarCarta(cartaDePinte, cartasJugadas, manoJugador)
		self.assertEqual(result, True)		

	def test_third_player_cant_follow(self):
		cartaDePinte = Card(0,0)
		cartasJugadas = [Card(3,1), Card(5,0), Card(6,2)]
		manoJugador = [Card(1,3), Card(6,2)]
		result = comprobarCarta(cartaDePinte, cartasJugadas, manoJugador)
		self.assertEqual(result, True)

	def test_third_player_chooses_to_not_follow(self):
		cartaDePinte = Card(0,0)
		cartasJugadas = [Card(3,1), Card(8,0), Card(1,2)]
		manoJugador = [Card(1,2), Card(6,0)]
		result = comprobarCarta(cartaDePinte, cartasJugadas, manoJugador)
		self.assertEqual(result, True)

	def test_third_player_chooses_to_follow(self):
		cartaDePinte = Card(0,0)
		cartasJugadas = [Card(3,1), Card(8,0), Card(6,0)]
		manoJugador = [Card(1,2), Card(6,0)]
		result = comprobarCarta(cartaDePinte, cartasJugadas, manoJugador)
		self.assertEqual(result, True)

	def test_third_player_should_follow(self):
		cartaDePinte = Card(0,0)
		cartasJugadas = [Card(3,1), Card(5,0), Card(6,0)]
		manoJugador = [Card(1,1), Card(6,0)]
		result = comprobarCarta(cartaDePinte, cartasJugadas, manoJugador)
		self.assertEqual(result, False)

if __name__ == '__main__':
    unittest.main()