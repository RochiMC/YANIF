from game.Suit import Suit
from game.Type import Type

class Card:
    """Class that represents the card"""

    def __init__(self, suit: Suit, type: Type):
        """
        Constructor method of the card class.

        Args:
            suit (Suit): Suit of the card
            value (int): Value of the card, number of points to add
            type (str): Type of the card (A,Q,K...)
        """
        self.suit = suit
        self.type = type
        
        
    def __str__(self):
        return "" + self.type.name + " " + str(self.suit)
    
    def get_type(self):
        """
        Function that returns the type of the card
        """
        return self.type

    def get_suit(self):
        """
        Function that returns the suit of the card
        """
        return self.suit

    @staticmethod
    def compare(a: 'Card', b: 'Card') -> int: 
        """
        Method that compares two cards
        
        Args:
            a: first card
            b: second card
            
        Returns:
            value of comparison
        """
        order = ["C_A","C_2","C_3","C_4","C_5","C_6","C_7","C_J","C_Q","C_K"]
        return order.index(a.type.name) - order.index(b.type.name)
