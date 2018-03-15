import inspect

from pytictactoe.field_type import FieldType


class BasePlayer:
    def __init__(self):
        self.field_type = None

    def choose_field(self, grid):
        raise NotImplementedError(str(inspect.stack()[1][3]))

    def after_decision(self, grid, won):
        pass

    def get_my_field_type(self):
        return self.field_type

    def get_other_player_field_type(self):
        if self.field_type == FieldType.O:
            return FieldType.X
        elif self.field_type == FieldType.X:
            return FieldType.O
        else:
            raise RuntimeError('Unknown FieldType for Player!')

    def __str__(self):
        return '<Player:{}>'.format(self.field_type.name)
