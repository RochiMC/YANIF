from typing import List
from game.Card import Card
from functools import cmp_to_key
from game.Suit import Suit
from game.Type import Type
from exception.CardExceptions import IllegalCardExtrationException

class Hand:
    """
    Class that defines the hand of a player
    """

    def __init__(self, cards: List[Card]):
        """
        Constructor method for the class Hand
        
        Args:
            cards: list of cards of the hand
        """
        
        self.cards = cards
        self.order_cards()

    def extract_card(self, indexes: list[int]):
        """
        Method that extracts the card in the index indexes
        
        Args:
            indexes: list with the indexes of the cards to extract
            
        Returns:
            the cards extracted
        """
        
        extracted_cards = []
        if len(indexes) == 1:
            # If there is only one index, extract it directly
            if indexes[0] >= len(self.cards):
                raise IllegalCardExtrationException("The index is bigger than legal")
            else:
                extracted_cards.append(self.cards.pop(indexes[0]))
            
        elif len(indexes) > 1:
            if(self.is_stair(indexes) or self.is_pair(indexes)):
                indexes.sort(reverse=True) #Extract from bigger to smaller so that we have no problems with the indexes
                for index in indexes:
                    extracted_cards.append(self.cards.pop(index))
            else:
                raise IllegalCardExtrationException("The selection of cards is invalid")
                
                
        return extracted_cards
    
    def is_stair(self, indexes: list[int]):
        """
        Function that, given a series of indexes returns if the selection is a stair
        
        Args:
            indexes: list of indexes to check
            
        Returns:
            True if it is a stair, False, otherwise
        """
        if len(indexes) <= 2:
            return False
        else:
            for i in range(0, len(indexes)-1):
                if indexes[i] >= len(self.cards) or indexes[i+1] >= len(self.cards):
                    raise IllegalCardExtrationException("The index is bigger than legal")
                else:
                    print(Card.compare(self.cards[indexes[i]], self.cards[indexes[i+1]]))
                    c1 = self.cards[indexes[i+1]]
                    c2 = self.cards[indexes[i]]
                    if Card.compare(c1, c2) != 1 or c1.get_suit() != c2.get_suit():
                        return False
        return True
        
    def is_pair(self, indexes: list[int]):
        """
        Function that, given a series of indexes returns if the selection is a pair/three
            
        Args:
            indexes: list of indexes to check
                
        Returns:
            True if it is a pair, False, otherwise
        """
        if indexes[0] >= len(self.cards):
            raise IllegalCardExtrationException("The index is bigger than legal")
        else:
            initial_type = self.cards[indexes[0]].get_type()
            
        for index in indexes[1:]:
            if index >= len(self.cards):
                raise IllegalCardExtrationException("The index is bigger than legal")
            elif self.cards[index].get_type() != initial_type:
                return False
        
        return True
           
    def order_cards(self):
        self.cards.sort(key=cmp_to_key(Card.compare))
  
    def add_card(self, card: Card):
        """
        Function that adds a certain card to the hand
        
        Args:
            card: card to add
        """
        self.cards.append(card)
        self.order_cards()
              
    def __str__(self):
        string = ""
        
        for c in self.cards:
            string += str(c) + " "
            
        return string

if __name__ == "__main__":
    c1 = Card(Suit.CLUBS, Type.C_A)
    c2 = Card(Suit.DIAMONDS, Type.C_5)
    c3 = Card(Suit.DIAMONDS, Type.C_6)
    c4 = Card(Suit.SPADES, Type.C_A)
    c5 = Card(Suit.SPADES, Type.C_7)
    
    h1 = Hand([c1,c2,c3,c4,c5])
    print(h1)
    h1.extract_card([0,1])
    print(h1)
    h1.add_card(Card(Suit.HEARTS, Type.C_4))
    print(h1)


