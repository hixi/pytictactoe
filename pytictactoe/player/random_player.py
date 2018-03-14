import random

from pytictactoe.player.base_player import BasePlayer


class RandomPlayer(BasePlayer):
    def choose_field(self, grid):
        allowed = False
        while not allowed:
            x, y = random_choice()
            allowed = yield x, y
            if allowed:
                yield None


def random_choice():
    return random.randint(0, 2), random.randint(0, 2)
