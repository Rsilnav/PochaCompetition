from IPlayer import IPlayer
from Card import Card

class DummyPlayer(IPlayer):

	def __init__(self):
		self.name = "Dummy"
		self.hand = []
		self.roundTrump = Card(0,0)

	def greet(self):
		print "Hello World!"

	def getName(self):
		return self.name

	def setInitialHand(self, hand):
		self.hand = hand

	def setTrumpCard(self, trumpCard):
		self.roundTrump = trumpCard;