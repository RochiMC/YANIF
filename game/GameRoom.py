from game.Deck import Deck
from game.Player import Player
from game.exception.RoomExceptions import *

class GameRoom:
    """
    Class that implements the main logic of the game
    """
    MAX_PLAYERS = 10
    players = list[Player]
    
    def __init__(self, room_id: str):
        """
        Constructor method of the class GameRoom
        """
        self.deck = Deck()
        self.players = []
        self.room_id = room_id
        
    def add_player(self, username: str):
        """
        Function that adds a player
        
        Args:
            player: new player to add
        """
        if len(self.players) >= self.MAX_PLAYERS:
            raise RoomFullException("The room is already full")
            
            
        self.players.append(Player(username))
    
        
    def check_player(self, username: str):
        """
        Function that checks whether a certain username was added to the game room
        
        Args:
            username: username to check

        Returns:
            True if it is, False otherwise
        """
        
        for p in self.players:
            print(p.get_name())
            if p.get_name() == username:
                return True
        
        return False
        
        
    def get_info(self, index: int):
        """
        Function that returns the information needed to actualise the view of the player index
        """
        string = ""
        
        for p in self.players:
            string += str(p) + " "
            
        return string