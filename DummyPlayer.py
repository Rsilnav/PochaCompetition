from IPlayer import IPlayer
from Card import Card

class DummyPlayer(IPlayer):

	def __init__(self, totalPlayers, idPlayer):
		self.name = "Dummy"
		self.hand = []
		self.roundTrump = Card(0,0)
		self.id = idPlayer
		self.totalPlayers = totalPlayers

	def greet(self):
		print "Hello World!"

	def getName(self):
		return self.name

	def setInitialHand(self, hand):
		self.hand = hand

	def setTrump(self, trumpCard):
		self.roundTrump = trumpCard

	def printHand(self):
		for card in self.hand:
			print card
