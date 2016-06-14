from IPlayer import IPlayer
from Card import Card

class DummyPlayer(IPlayer):

	def __init__(self):
		self.name = "Dummy"
		self.hand = []
		#self.roundTrump = Card(0,0)
		#self.id = idPlayer
		#self.order = []
		
	def setTotalPlayers(self, totalPlayers):
		self.totalPlayers = totalPlayers

	def greet(self):
		print "Hello World!"

	def getName(self):
		return self.name

	def setInitialHand(self, hand):
		self.hand = hand

	def setTrump(self, trumpCard):
		self.roundTrump = trumpCard

	def setOrder(self, order):
		self.order = order

	def giveBets(self, bets):
		pass

	def getBet(self):
		return 0

	def getCard(self, otherPlayerCards, playerOrder): 
		return self.hand[0]

	def printHand(self):
		for card in self.hand:
			print card
