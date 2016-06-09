class IPlayer:
	# Prints a personal greeting (< 20 char)
	def greet(self): raise NotImplementedError

	# Gets the hardcoded name for the player
	def getName(self): raise NotImplementedError

	# Sets initial hand at the start of every round
	def setInitialHand(self, hard): raise NotImplementedError