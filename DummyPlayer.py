from IPlayer import IPlayer

class DummyPlayer(IPlayer):

	def __init__(self):
		self.name = "Dummy"

	def greet(self):
		print "Hello World!"

	def getName(self):
		return self.name
