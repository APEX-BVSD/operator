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
        '''
        applies the effect of the card

        num: number effect is being done on
        '''
        match self._operation:
            case "ADD":
                return num + self._value
    
    def meets_conditions(self, base: int, index: int) -> bool:
        '''
        checks if uhhh if something meets conditions, Liz you're going to need to fill this one out
        '''
        return True


#class AddingCard():
#    def apply(number):
#        return number+2

#class MultiplyCard():
#    def apply(number):
#        return number*2
    