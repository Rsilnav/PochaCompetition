from DummyPlayer import *
from Card import *
from Deck import *

def playRound(players, deck, dealtCardsPerPlayer, firstPlayer):
	# Correction check
	dealtCardsNumber = len(players) * dealtCardsPerPlayer
	if dealtCardsNumber > 40:
		raise Exception

	# Deal cards
	dealtCards = [[] for i in xrange(len(players))]
	for i in xrange(len(players)):
		pId = (i+firstPlayer) % len(players)
		dealtCards[pId] = deck.cards[i*dealtCardsPerPlayer:(i+1)*dealtCardsPerPlayer]
		players[pId].setInitialHand(dealtCards[pId])
		if(dealtCardsNumber < 40):
			players[pId].setTrump(deck.cards[dealtCardsNumber])
		else:
			players[pId].setTrump(deck.cards[39])

	# Ask for the bets
	lastWinner = firstPlayer
	order = []
	bets = [0,0,0,0]
	previousBets = []
	for i in xrange(len(players)):
		order.append((i+lastWinner) % len(players))
		bet = players[order[i]].getBet(previousBets)
		bets[order[i]] = bet
		previousBets.append(bet)
	# Play all turns
	for i in xrange(dealtCardsPerPlayer):
		order = []
		for i in xrange(len(players)):
			order.append((i+lastWinner) % len(players))
		for i in order:
			#pedir carta diciendo cuales hay en la mesa
			pass
		# Calculate winner

	# Compare bets with won turns and get points of this round
	return [0,0,0,0]

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

def main():
	playStaticGame(1,10)

if __name__ == '__main__':
	main()
