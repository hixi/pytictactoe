import random

from pytictactoe.player.base_player import BasePlayer


class RandomPlayer(BasePlayer):
    def choose_field(self, grid):
        allowed = False
        empty_fields = grid.get_empty_fields()
        field = empty_fields[random.randint(0, len(empty_fields) - 1)]
        while not allowed:
            allowed = yield field
            if allowed:
                yield None
