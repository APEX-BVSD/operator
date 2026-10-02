class Player:
    __cards: list = []
    __score_cards: list = []
    __score: int = 0
    __high_score: int = 0
    __round: int = 0

    def add_card(self, card):
        self.__cards.append(card)

    def swap_card_order(self):
        pass

    def calculate_score(self, base: int):
        card_index: int = 0
        for card in self.__cards:
            card_index += 1
            try:
                if card.meets_conditions(base, card_index):
                    card.apply(self.__score)
            except:
                print("invalid card/type error")

    def bonus_score(self):
        if self.__score_cards != []:
            for card in self.__score_cards:
                try:
                    self.__score = card.apply(self.__score)
                except:
                    print("invalid card/type error")
    
    def get_score(self):
        return self.__score