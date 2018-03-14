from pytictactoe.field_type import FieldType


class Grid:
    def __init__(self):
        self.fields = [
            [FieldType.EMPTY, FieldType.EMPTY, FieldType.EMPTY],
            [FieldType.EMPTY, FieldType.EMPTY, FieldType.EMPTY],
            [FieldType.EMPTY, FieldType.EMPTY, FieldType.EMPTY]
        ]

    def get_rows(self):
        return self.fields

    def get_columns(self):
        return [
            [self.fields[0][0], self.fields[1][0], self.fields[2][0]],
            [self.fields[0][1], self.fields[1][1], self.fields[2][1]],
            [self.fields[0][2], self.fields[1][2], self.fields[2][2]],
        ]

    def get_diagonals(self):
        return [
            [self.fields[0][0], self.fields[1][1], self.fields[2][2]],
            [self.fields[0][2], self.fields[1][1], self.fields[2][0]],
        ]

    def set_field(self, field, field_type):
        if self.fields[field.x][field.y] == FieldType.EMPTY:
            self.fields[field.x][field.y] = field_type
            return True
        else:
            return False
