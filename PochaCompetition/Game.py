from DummyPlayer import *
from Card import *
from Deck import *

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

def main():
	playStaticGame(1,10)

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