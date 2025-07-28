from typing import List, Dict, Optional
from game.GameRoom import GameRoom

class RoomsManager:
    """"
    Class that implements the Manager of GameRooms
    """
    
    rooms : Dict[str, GameRoom] = {}
    
    
    def add_room(self, room_id: str):
        """
        Function that adds a new room in the room Manager
        
        Args:
            room_id: id of the room to add
        """
        self.rooms[room_id] = GameRoom(room_id)
    
    def add_player(self, room_id: str, username: str):
        """
        Function that adds a certain player to the room room id
        
        Args:
            room_id: the id of the room to add the player
            username: username of the player to add
        """
        
        if room_id in self.rooms.keys():
            self.rooms[room_id].add_player(username)
            
    def room_exists(self, room_id: str):
        """
        Function that returns whether a certain room exists
        """
        
        return room_id in self.rooms.keys()
    
    def check_username(self, username: str, room_id: str):
        """
        Function that checks whether a username has been added to a certain room 
        
        Args:
            username: username to check
            room_id: room in which the username needs to have been added
        """
        
        if room_id in self.rooms.keys():
            self.rooms[room_id].check_player(username)