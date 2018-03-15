import random

from pytictactoe.field import Field
from pytictactoe.field_type import FieldType
from pytictactoe.player import ai_service
from pytictactoe.player.base_player import BasePlayer


class CleverPlayer(BasePlayer):

    def get_str_player(self):
        if self.get_my_field_type() == FieldType.X:
            return 'X'
        elif self.get_my_field_type() == FieldType.O:
            return 'O'
        else:
            raise RuntimeError('Unknown FieldType for Player')


    def grid_to_list(self,grid):
        s = ''
        for y in range (0,3):
            for x in range (0, 3):
                if grid.get_field(x, y) == FieldType.EMPTY:
                    s += '-'
                elif grid.get_field(x, y) == FieldType.O:
                    s += 'O'
                elif grid.get_field(x, y) == FieldType.X:
                    s += 'X'
                else:
                    raise RuntimeError('Unkwon FieldType on Board')

        return s

    def choose_field(self, grid):
        grid_str = self.grid_to_list(grid)
        player_str = self.get_str_player()

        cost, move = ai_service.nextMove(list(grid_str), player_str)

        x = int(move % 3)
        y = int(move / 3)


        allowed = False
        while not allowed:
            field = Field(x, y)
            allowed = yield field
            if allowed:
                yield None
            else:
                print("Try it again, field is already chosen.\n")