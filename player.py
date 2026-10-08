from cards import *

class Player:
    _cards: list = []
    _score_cards: list = []
    _score: int = 0

    def add_card(self, card):
        '''
        
        '''
        self._cards.append(card)

    def swap_card_order(self, a: int, b: int):
        '''
        
        '''
        _temp_card: Card = self._cards[a]
        self._cards[a] = self._cards[b]
        self._cards[b] = _temp_card

    def calculate_score(self, base: int):
        '''
        
        '''
        self._score += base
        card_index: int = 0
        try:
            for card in self._cards:
                try:
                    if card.meets_conditions(base, card_index):
                        card.apply(self._score)
                    else:
                        pass
                except:
                    print("invalid card/type error 1")
                card_index += 1
        except:
            print("No cards")

    """
    Optional, but it was easy to implement so I added it here. If we decide that it would be a good design decision
        to cumulatively increase the player's total score at the end of each round, that's what this method will do.

        Untested, since we haven't decided if we should use it, it's mostly here as a reminder to myself.

        -Liz
    """
    def bonus_score(self):
        '''
        
        '''
        if self._score_cards != []:
            for card in self._score_cards:
                try:
                    self._score = card.apply(self._score)
                except:
                    print("invalid card/type error 2")
    
    def get_score(self):
        '''
        
        '''
        return self._score