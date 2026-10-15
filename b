
class HorizontalList(CardList):

    _card_list: list = [Placeholder1(), Placeholder2(), Placeholder3(), Placeholder4()]
    _x_offset: int = 200
    _y_offset: int = 400

    def process_click(self, x, y):
        '''
        Processes a click by checking if it is within an interactable object

        X: the x coordinate of the click
        Y: the y coordinate of the click
        '''

        counter: int = 0 

        for object in self._card_list:
            if x >= object.hitbox.left + object.position[0] and x <= object.hitbox.right + object.position[0] and y >= object.hitbox.top + object.position[1] and y <= object.hitbox.bottom + object.position[1]:
                self._dragged_object = object
                self._dragged_sprite = pygame.Surface.copy(object.image)
                self._dragged_index = counter
                pygame.Surface.set_alpha(self._dragged_sprite, 100)
            counter += 1

    def check_card_movement(self, x, y, list, index):
        '''
        Checks if cards need to be moved after a drag stops

        X: the x coordinate of the cursor
        Y: the y coordinate of the cursor    
        '''
        
        if x >= self._x_offset and x <= (len(self._card_list) + 1) * 100 - 50 + self._x_offset and y <= self._card_list[0].hitbox.bottom + self._card_list[0].position[1] and y >= self._card_list[0].hitbox.top + self._card_list[0].position[1]:
            new_index: int = (x - 50 - self._x_offset) // 100 + 1
            if list == self:
                if new_index > index:
                    self._card_list.insert(new_index, self._card_list[index])
                    list._card_list.pop(index)

                elif index == new_index:
                    pass

                else:
                    self._card_list.insert(new_index, self._card_list[index])
                    list._card_list.pop(index + 1)
            else:
                self._card_list.insert(new_index, list._card_list[index])
                list._card_list.pop(index)

        self._dragged = False
        

    def set_card_position(self):
        counter: int = 0
        for card in self._card_list:
            card.position = (100 * counter + self._x_offset, self._y_offset)
            counter += 1