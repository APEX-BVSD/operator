"""
Contains all of the cards in play.
September | 2026
Carter Quarles
Elizabeth Posusta
First Last 
"""

from enum import Enum

class PossibleCondition(Enum):
    IS_NTH = 0,
    BASE_IS_EVEN = 1,
    BASE_IS_FACTOR = 2,
    BASE_IS_MULTIPLE = 3,

class Condition:
    _conditions: list[PossibleCondition] = list()
    _n = 0

    def __init__(self, n: int, cond: list[PossibleCondition] | None = None):
        self._n = n
        if cond:
            for c in cond:
                self._conditions.append(c)

    def check(self, base: int):
        if len(self._conditions) == 0:
            return True
        match self

class Card():
    _value: int = 15
    _operation: str = "ADD"

    def apply(self, num: int):
        match self._operation:
            case "ADD": # Addition
                return num + self._value
            case "MUL": # Multiplication
                return num * self._value
            case "DVR": # Division with remainder added
                return num / self._value + num % self._value
            case "SUB": # Subtraction
                return num - self._value
    
    def meets_conditions(self, base: int, index: int) -> bool:
        return True


#class AddingCard():
#    def apply(number):
#        return number+2

#class MultiplyCard():
#    def apply(number):
#        return number*2
    