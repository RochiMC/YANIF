from game.Card import Card
from game.Type import Type
from game.Suit import Suit
import random
from typing import List


class Deck:
    """Class that implements the Deck of the game"""
    main_deck : list[Card]
    discard_deck : list[Card]
    last_discard : list[Card]
    
    def __init__(self):
        """
        Constructor method of the deck class
        """
        self.main_deck = []
        self.discard_deck = []
        self.last_discard = []
        for type in Type:
            for suit in Suit:
                self.main_deck.append(Card(suit, type))
                
        self.shuffle()
        self.last_discard.append(self.main_deck.pop(0))
                   
    def shuffle(self):
        """
        Function that shuffles the main deck
        """
        random.shuffle(self.main_deck)
        
    def extract_main_deck(self):
        """
        Function that extracts a card from the main deck
        """
        
        extracted_card = self.main_deck.pop(0)
        
        # If the card extracted was the last one, change the discard to the main except the last card and shuffle again
        if len(self.main_deck) == 0:
            self.main_deck = self.discard_deck[1:]
            self.discard_deck = self.discard_deck[0]
            self.shuffle()
            
        return extracted_card

    def extract_last_discard(self, index: int):
        """
        Function that extracts a card from the dicard deck
        """
        return self.last_discard.pop(index)
    
    def set_last_discard(self, cards: List[Card]):
        """
        Function that sets the last discard
        
        Args:
            cards: list of the cards to add to the discard card
        """
        
        # First add all the cards of the last discard to the discard deck
        for card in self.last_discard:
            self.discard_deck.append(card)
            
        # Set the new cards to the last discard
        self.last_discard = []
        if isinstance(cards, list):
            self.last_discard.extend(cards)
        else:
            self.last_discard.append(cards)
    
    def __str__(self):
        string = "Main deck:\n"
        for card in self.main_deck:
            string += str(card) + " "
            
        string += "\nLast discard:\n"
        for card in self.last_discard:
            string += str(card) + " "
            
        return string
            
        
if __name__ == "__main__":
    d = Deck()
    print(d)
    d.set_last_discard([d.extract_main_deck(), Card(Suit.CLUBS, Type.C_3)])
    print(d)