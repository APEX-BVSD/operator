import copy

from cards import *


class Player:
    game_state: str = "START_SCREEN"

    def __init__(self):
        self._score = 9999
        self._cards: list[Card] = []
        # self._score_cards: list[Card] = []
        self._score_cards: list[Card] = []
        # for _ in range(5):
        #     self._cards.append(random_card(0))
        # for _ in range(5):
        #     self._score_cards.append(random_card(0))

    def add_card(self, card):
        self._cards.append(card)

    def add_scoring_card(self, card):
        self._score_cards.append(card)

    def swap_card_order(self, a: int, b: int):
        _temp_card: Card = self._cards[a]
        self._cards[a] = self._cards[b]
        self._cards[b] = _temp_card

    def calculate_score(self, base: int, cards):
        card_index: int = 0
        try:
            for card in cards:
                try:
                    if card.meets_conditions(base, card_index):
                        base = card.apply(int(base))
                        print(base, card._operation, card.get_number())
                    else:
                        pass
                except:
                    print("invalid card/type error 1")
                card_index += 1
        except:
            print("No cards")
        self._score += base

    """
    Optional, but it was easy to implement so I added it here. If we decide that it would be a good design decision
        to cumulatively increase the player's total score at the end of each round, that's what this method will do.

        Untested, since we haven't decided if we should use it, it's mostly here as a reminder to myself.

        -Liz
    """

    def bonus_score(self):
        if self._score_cards != []:
            for card in self._score_cards:
                try:
                    self._score = card.apply(self._score)
                except:
                    print("invalid card/type error 2")

    def get_score(self):
        return self._score

    def get_cards(self) -> list[Card]:
        return copy.copy(self._cards)

    def set_cards(self, cards: list[Card]) -> None:
        self._cards = cards

    def get_score_cards(self) -> list[Card]:
        return self._score_cards

    def set_score(self, score):
        self._score = score
