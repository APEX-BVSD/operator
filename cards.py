"""
Card class and helper functions
September | 2026
Carter Quarles
Elizabeth Posusta
First Last 
"""

import random

from enum import IntEnum

class PossibleCondition(IntEnum):
    IS_NTH = 1,
    FACTORS_INTO_BASE = 2

class Condition:
    _conditions: PossibleCondition | None = None
    _n: int = 0
    _v: int = 0

    def __init__(self, n: int | None = None, v: int | None = None, cond: PossibleCondition | None = None):
        self._n = n
        self._v = v
        if cond != None:
            self._conditions = cond

    def check(self, base: int, pos: int):
        if self._conditions == None:
            return True
        else:
            match self._conditions:
                case PossibleCondition.IS_NTH:
                    if pos == self._n:
                        return True
                case PossibleCondition.FACTORS_INTO_BASE:
                    if base % self._v == 0:
                        return True
        return False



class Card():
    _value: int = 0
    _operation: str = "ADD"
    _condition: Condition = Condition()

    def __init__(self, v: int, o: str, c: Condition):
        self._value = v
        self._operation = o
        self._condition = c

    def apply(self, num: int):
        match self._operation:
            case "ADD": # Addition
                return num + self._value
            case "MUL": # Multiplication
                return num * self._value
            case "DIV": # Division with remainder ignored
                return num / self._value
            case "SUB": # Subtraction
                return num - self._value
    
    def meets_conditions(self, base: int, pos: int) -> bool:
        return self._condition.check(base, pos)
    
    def get_number(self):
        return self._value

"""
    Instantiate a new, randomized Card
"""
def random_card(difficulty: int) -> Card:
    # Janky coinflip to decide if the number will be a decimal. Becomes more likely as the game goes on/`difficulty` is increased.
    #   Also used to determine conditions
    coinflip: int = random.randint(0, 5 * difficulty)
    if coinflip > difficulty * 2: # Arbitrary threshold. Needs to be refined/tested for balance
        v: float = random.random() * 10 * difficulty / 2 # Yet another arbitrary threshold that needs logic.
        v = round(v, 1)
    else:
        v: int = random.randint(0, 5 + difficulty * 2) # You'll never guess what this is!
    
    if coinflip > int(difficulty * 2.5):
        c: Condition = Condition(random.randint(0, 5), v, PossibleCondition(random.randint(1, 2)))
    else:
        c: Condition = Condition()

    o: str = "ADD"
    operation_coinflip: int = random.randint(1, 4)
    match operation_coinflip:
        case 1:
            o = "ADD"
        case 2:
            o = "SUB"
        case 3:
            o = "MUL"
        case 4:
            o = "DIV"

    return Card(v, o, c)