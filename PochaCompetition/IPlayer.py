class IPlayer:
	# Prints a personal greeting (< 20 char).
	def greet(self): raise NotImplementedError

	# Gets the hardcoded name for the player.
	def getName(self): raise NotImplementedError

	# Sets initial hand at the start of every round.
	def setInitialHand(self, hand): raise NotImplementedError

	# Sets trump card for current round.
	def setTrump(self, trumpCard): raise NotImplementedError

	# Informs the player of the order for this turn.
	def setOrder(self, order): raise NotImplementedError

	# Ask the player for his initial bet. At this point he has cards, trump card and
	# knows order of playing.
	def getBet(self): raise NotImplementedError

	# Ask the player for a card. He is given the current cards of the table,
	# and the order of the turn.
	def getCard(self, otherPlayerCards, playerOrder): raise NotImplementedError
	
	# Print player's cards.
	def printHand(self): raise NotImplementedError

	def giveBets(self, bets): raise NotImplementedError
