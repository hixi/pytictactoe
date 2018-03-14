import inspect

from pytictactoe.field_type import FieldType


class BasePlayer:
    def __init__(self, field_type=FieldType.X):
        self.field_type = field_type

    def choose_field(self, grid):
        raise NotImplementedError(str(inspect.stack()[1][3]))

    def __str__(self):
        return '<Player:{}>'.format(self.field_type.name)
