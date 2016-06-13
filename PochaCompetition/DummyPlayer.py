from IPlayer import IPlayer
from Card import Card

class DummyPlayer(IPlayer):

	def __init__(self, totalPlayers, idPlayer):
		self.name = "Dummy"
		self.hand = []
		self.roundTrump = Card(0,0)
		self.id = idPlayer
		self.totalPlayers = totalPlayers
		self.order = []

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

	def getBet(self, previousBets):
		restriction = -1
		# Nos aseguramos de no ser los ultimos en apostar. Si lo somos,
		# la suma de las apuestas no puede ser igual a la cantidad de cartas repartidas
		if len(previousBets) == (self.totalPlayers - 1):
			restriction = len(self.hand) - sum(previousBets)
		myBet = 0
		if myBet != restriction:
			return myBet
		else:
			return myBet + 1

	def getCard(self, otherPlayerCards, playerOrder): raise NotImplementedError

	def printHand(self):
		for card in self.hand:
			print card
