"""
Contains all of the cards in play.
September | 2026
Carter Quarles
Elizabeth Posusta
First Last 
"""

class Card():
    _value: int = 15
    _operation: str = "ADD"

    def apply(self, num: int):
        match self._operation:
            case "ADD":
                return num + self._value
    
    def meets_conditions(self, base: int, index: int) -> bool:
        return True


#class AddingCard():
#    def apply(number):
#        return number+2

#class MultiplyCard():
#    def apply(number):
#        return number*2
    