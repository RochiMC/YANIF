class RoomFullException(Exception):
    def __init__(self, message):
        super().__init__(message)
        
        
class DupplicatedUsernameException(Exception):
    def __init__(self, message):
        super().__init__(message)