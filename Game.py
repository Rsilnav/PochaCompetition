from models.DummyPlayer import *
from utils.Card import *
from utils.Deck import *

def playStaticRound(deck, cardsPerRound, player1, player2, player3, player4):
	return [0,0,0,0]

def playStaticGame(cardsPerRound = 10, rounds = 20):
	inititalDeck = Deck()
	inititalDeck.shuffle()

	player1 = DummyPlayer()
	player2 = DummyPlayer()
	player3 = DummyPlayer()
	player4 = DummyPlayer()

	points = [0, 0, 0, 0]

	for round in xrange(rounds):
		deck = inititalDeck
		newPoints = playStaticRound(deck, cardsPerRound, player1, player2, player3, player4)
		points = map(sum, zip(points, newPoints))

	print points

def main():
	playStaticGame()

if __name__ == '__main__':
	main()