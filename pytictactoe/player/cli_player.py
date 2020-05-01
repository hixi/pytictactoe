from pytictactoe.field import Field
from pytictactoe.player.base_player import BasePlayer


class CliPlayer(BasePlayer):
    def choose_field(self, grid):
        print(grid)
        allowed = False
        while not allowed:
            field = _choose_field_input()
            allowed = yield field
            if allowed:
                yield None
            else:
                print("Try it again, field is already chosen.\n")


def _choose_field_input():
    x_index = _input_field('x')
    y_index = _input_field('y')
    return Field(x=x_index, y=y_index)


def _input_field(axis):
    while True:
        try:
            index = int(input("Please chose {}-coordinate from 0 to 2: \n".format(axis)))
            if index in range(0, 3):
                return index
            else:
                print("Sorry, no valid coordinate.\n")
                continue
        except ValueError:
            print("Sorry, I didn't understand that.\n")
            continue
