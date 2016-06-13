from Card import *
import random
class Deck():

	def __init__(self):
		self.cards = []
		for number in xrange(10):
			for suit in xrange(4):
				self.cards.append(Card(number, suit))

	def __str__(self):
		toPrint = ""
		for card in self.cards:
			toPrint += str(card.getNumber()) + " - " + str(card.getSuit()) + "\n"
		return toPrint

	def show(self):
		for card in self.cards:
			print card

	def shuffle(self):
		random.shuffle(self.cards)