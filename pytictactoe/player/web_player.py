from pytictactoe.field import Field
from pytictactoe.player.base_player import BasePlayer


class WebAPIPlayer(BasePlayer):
    def __init__(self, next_move):
        super().__init__()
        self.next_move = next_move

    def choose_field(self, grid):
        allowed = yield Field(self.next_move['x'], self.next_move['y'])
        if allowed:
            yield None
        else:
            raise Exception("Try it again, field is already chosen.")
