import unittest
from PochaCompetition.Card import Card

class TestUM(unittest.TestCase):
 
    def setUp(self):
        pass

    def test_card_names(self):
    	a = Card(0, 0)
    	self.assertEqual(a.show(), "Dos de Oros")
    	a = Card(0, 1)
    	self.assertEqual(a.show(), "Dos de Copas")
    	a = Card(0, 2)
    	self.assertEqual(a.show(), "Dos de Espadas")
    	a = Card(0, 3)
    	self.assertEqual(a.show(), "Dos de Bastos")

    def test_card_suits(self):
        a = Card(0, 0)
        self.assertEqual(a.getSuit(), 0)
        a = Card(0, 1)
        self.assertEqual(a.getSuit(), 1)
        a = Card(0, 2)
        self.assertEqual(a.getSuit(), 2)
        a = Card(0, 3)
        self.assertEqual(a.getSuit(), 3)

    def test_card_numbers(self):
        a = Card(0, 0)
        self.assertEqual(a.getNumber(), 0)
        a = Card(1, 0)
        self.assertEqual(a.getNumber(), 1)
        a = Card(2, 0)
        self.assertEqual(a.getNumber(), 2)
        a = Card(3, 0)
        self.assertEqual(a.getNumber(), 3)
        a = Card(4, 0)
        self.assertEqual(a.getNumber(), 4)
        a = Card(5, 0)
        self.assertEqual(a.getNumber(), 5)
        a = Card(6, 0)
        self.assertEqual(a.getNumber(), 6)
        a = Card(7, 0)
        self.assertEqual(a.getNumber(), 7)
        a = Card(8, 0)
        self.assertEqual(a.getNumber(), 8)
        a = Card(9, 0)
        self.assertEqual(a.getNumber(), 9)

    def test_card_print(self):
        a = Card(0, 0)
        self.assertEqual(str(a), "Dos de Oros")

if __name__ == '__main__':
    unittest.main()