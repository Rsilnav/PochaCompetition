from DummyPlayer import *
from Card import *
from Deck import *

def playRound(players, deck, dealtCardsPerPlayer, firstPlayer):
	# Correction check
	dealtCardsNumber = len(players) * cardsPerRound
	if dealtCardsNumber > 40:
		raise Exception
	# Deal cards
	for i in xrange(len(players)):
		pId = (i+firstPlayer) % len(players)
		players[pId].setInitialHand(deck.cards[i*dealtCardsPerPlayer:(i+1)*dealtCardsPerPlayer])
		if(dealtCardsNumber < 40):
			players[pId].setTrump(deck.cards[dealtCardsNumber])
		else:
			players[pId].setTrump(deck.cards[40])
	# Ask for the bets
	lastWinner = firstPlayer
	order = []
	for i in xrange(len(players):
		order.append((i+lastWinner)% len(players))
	return [0,0,0,0]

def playStaticGame(cardsPerRound = 10, rounds = 20):
	inititalDeck = Deck()
	inititalDeck.shuffle()

	player1 = DummyPlayer()
	player2 = DummyPlayer()
	player3 = DummyPlayer()
	player4 = DummyPlayer()

	points = [0, 0, 0, 0]
	players = [player1, player2, player3, player4]
	for round in xrange(rounds):
		deck = inititalDeck
		newPoints = playRound(players, deck, cardsPerRound, 0)
		points = map(sum, zip(points, newPoints))

	print points

def main():
	playStaticGame()

if __name__ == '__main__':
	main()