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
        if self.fields[field.y][field.x] == FieldType.EMPTY:
            self.fields[field.y][field.x] = field_type
            return True
        else:
            return False

    def get_field(self, x, y):
        return self.fields[y][x]


    def is_winning_state(self):
        winning_states = [self.get_rows(), self.get_columns(), self.get_diagonals()]
        print(winning_states)
        for winning_state in winning_states:
            for w in winning_state:
                if not (w[0] == w[1] and w[1] == w[2] and w[2] == w[0]):
                    return False

        if self.count_empty_fields() == 0:
            return True
        return False

    def count_empty_fields(self):
        counter = 0
        for field_list in self.fields:
            for field in field_list:
                if field == FieldType.EMPTY:
                    counter = counter + 1
        return counter

    def __str__(self):
        field_string = '\n    0   1   2\n'
        field_string += '  ' + '-' * 13 + '\n'
        for i, row in enumerate(self.fields):
            field_string += '{} '.format(i)
            for field in row:
                field_content = ' ' if field == FieldType.EMPTY else field.name
                field_string += '| {} '.format(field_content)
            field_string += '|\n' + '  ' + '-' * 13 + '\n'
        return field_string
