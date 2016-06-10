class IPlayer:
	# Prints a personal greeting (< 20 char)
	def greet(self): raise NotImplementedError

	# Gets the hardcoded name for the player
	def getName(self): raise NotImplementedError

	# Sets initial hand at the start of every round
	def setInitialHand(self, hand): raise NotImplementedError

	# Sets trump card for current round
	def setTrump(self, trumpCard): raise NotImplementedError