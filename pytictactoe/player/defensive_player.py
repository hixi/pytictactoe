import random

from pytictactoe.field import Field
from pytictactoe.field_type import FieldType, get_opponent_field_type
from pytictactoe.player.base_player import BasePlayer


class DefensivePlayer(BasePlayer):
    def _threat(self, triple):
        assert len(triple) == 3
        number_of_enemy_stones = len(list(filter(lambda x: x == get_opponent_field_type(self), triple)))
        number_of_empty_stones = len(list(filter(lambda x: x == FieldType.EMPTY, triple)))

        return number_of_enemy_stones == 2 and number_of_empty_stones == 1

    def find_best_field(self, grid):
        defense_list = []
        for i, triple in enumerate(grid.get_rows()):
            if self._threat(triple):
                for j in range(0, 3):
                    defense_list.append(Field(j, i))

        for i, triple in enumerate(grid.get_columns()):
            if self._threat(triple):
                for j in range(0, 3):
                    defense_list.append(Field(i, j))

        return defense_list

    def choose_field(self, grid):
        defense_list = self.find_best_field(grid)
        random.shuffle(defense_list)
        if len(defense_list) > 0:
            allowed = False
            while not allowed:
                field = defense_list.pop()
                allowed = yield field
                if allowed:
                    yield None

        else:
            allowed = False
            while not allowed:
                field = Field(x=random.randint(0, 2), y=random.randint(0, 2))
                allowed = yield field
                if allowed:
                    yield None
