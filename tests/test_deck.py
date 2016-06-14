import unittest
from PochaCompetition.Deck import Deck

class TestUM(unittest.TestCase):

    def setUp(self):
        pass

    def test_deck_cards_numbers(self):
        deck = Deck()
        for card in deck.cards:
            self.assertIn(card.getNumber(), range(10))

    def test_deck_cards_suit(self):
        deck = Deck()
        for card in deck.cards:
            self.assertIn(card.getSuit(), range(4))

    def test_deck_init(self):
        deck = Deck()
        self.assertEqual(len(deck.cards), 40)

    def test_deck_shuffle(self):
        deck = Deck()
        cards = deck.cards[:]
        deck.shuffle()
        equals = cards == deck.shuffle()
        self.assertEqual(equals, False)

    def test_deck_str(self):
        deck = Deck()
        string = ""
        for card in deck.cards:
            string += "{} - {}\n".format(card.getNumber(), card.getSuit())

        self.assertEqual(str(deck), string)

