from enum import Enum

class Type(Enum):
    C_A = ("A", 1)
    C_2 = ("2", 2)
    C_3 = ("3", 3)
    C_4 = ("4", 4)
    C_5 = ("5", 5)
    C_6 = ("6", 6)
    C_7 = ("7", 7)
    C_J = ("J", 10)
    C_Q = ("Q", 10)
    C_K = ("K", 10)
    
    def __init__(self, nombre, valor):
        self._nombre_carta = nombre
        self._valor_carta = valor

    def __str__(self):
        return self._nombre_carta

    @property
    def valor(self):
        return self._valor_carta