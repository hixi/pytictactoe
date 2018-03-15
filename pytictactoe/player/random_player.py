import random

from pytictactoe.field import Field
from pytictactoe.player.base_player import BasePlayer


class RandomPlayer(BasePlayer):
    def choose_field(self, grid):
        allowed = False
        empty_fields = grid.get_empty_fields()
        while not allowed:
            field = Field(x=random.randint(0, 2), y=random.randint(0, 2))
            allowed = yield field
            if allowed:
                yield None
