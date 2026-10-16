from cards import *
from settings import *
from cardlists import *

class Player:
    cards: CardList = CardList(list(), BOTTOM_LIST_TOP_LEFT[0], BOTTOM_LIST_TOP_LEFT[1], False)
    score_cards: CardList = CardList(list(), SIDE_LIST_TOP_LEFT[0], SIDE_LIST_TOP_LEFT[1], True)
    _score: int = 0

    """
        Add `card` to player hand
    """
    def add_card(self, card):
        self.cards.card_list.append(card)

    """
        Add `card` to player score deck
    """
    def add_score_card(self, card):
        self.score_cards.card_list.append(card)

    def calculate_score(self, base: int):
        self._score += base
        card_index: int = 0
        try:
            for card in self.cards.card_list:
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

    def bonus_score(self):
        if self.score_cards.card_list != []:
            for card in self.score_cards.card_list:
                try:
                    self._score = card.apply(self._score)
                except:
                    print("invalid card/type error 2")
    
    def get_score(self):
        return self._score