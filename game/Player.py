class Player:
    """ Class that implements the player"""
    DEATH_LIMIT = 200
    
    def __init__(self, name: str):
        """ 
        Contructor function of the class player
        """
        self.name: str = name
        self.points = 0
        self.turn = False
        self.dead = False
        
        
    def add_points(self, points : int):
        """
        Function that changes the points of the player
        
        Args:
            points: number of points to add
        """
        
        self.points += points
        
        # If the number of points is larger than DEATH_LIMIT, set the player as dead
        if self.points > self.DEATH_LIMIT:
            self.dead = True
            
        # If the number of points is 100 or 200, then set the points to half of it
        if self.points == 100 or self.points == 200:
            self.points = self.points/2
            
    def set_turn(self, turn: bool):
        """
        Function that changes the turn of the player
        
        Args:
            turn: bool with the turn
        """
        self.turn = turn
        
    def get_name(self):
        """
        Function that returns the name of the player
        
        """
        return self.name