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

    def __str__(self):
        field_string = '    0   1   2\n'
        field_string += '  ' + '-' * 13 + '\n'
        for i, row in enumerate(self.fields):
            field_string += '{} '.format(i)
            for field in row:
                field_content = ' ' if field == FieldType.EMPTY else field.name
                field_string += '| {} '.format(field_content)
            field_string += '|\n' + '  ' + '-' * 13 + '\n'
        return field_string
