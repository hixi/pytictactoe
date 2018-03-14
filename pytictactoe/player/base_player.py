import inspect

from pytictactoe.player.player_type import PlayerType


class BasePlayer:
    def __init__(self, player_type=PlayerType.X):
        self.player_type = player_type

    def choose_field(self, grid):
        raise NotImplementedError(str(inspect.stack()[1][3]))
