class Card():
	def __init__(self, number, suit):
		self.number = number
		self.suit = suit

	def __str__(self):
		numberName = ["Dos", "Cuatro", "Cinco", "Seis", "Siete", "Sota", "Caballo", "Rey", "Tres", "As"]
		suitName = ["Oros", "Copas", "Espadas", "Bastos"]
		return '{0} de {1}'.format(numberName[self.number], suitName[self.suit])

	def __eq__(self, other):
		return self.suit == other.suit and self.number == other.number

	def getNumber(self):
		return self.number

	def getSuit(self):
		return self.suit

	def show(self):
		numberName = ["Dos", "Cuatro", "Cinco", "Seis", "Siete", "Sota", "Caballo", "Rey", "Tres", "As"]
		suitName = ["Oros", "Copas", "Espadas", "Bastos"]
		return '{0} de {1}'.format(numberName[self.number], suitName[self.suit])