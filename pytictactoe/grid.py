import json

from pytictactoe.field import Field
from pytictactoe.field_type import FieldType

string_to_field_type = dict(
    zip(["", 'X', 'O'], [FieldType.EMPTY, FieldType.X, FieldType.O]))
field_type_to_string = dict(
    zip([FieldType.EMPTY, FieldType.X, FieldType.O], ["", 'X', 'O']))


class Grid:
    def __init__(self, grid_config=None):
        if not grid_config:
            self.fields = [
                [FieldType.EMPTY, FieldType.EMPTY, FieldType.EMPTY],
                [FieldType.EMPTY, FieldType.EMPTY, FieldType.EMPTY],
                [FieldType.EMPTY, FieldType.EMPTY, FieldType.EMPTY]
            ]
        else:
            self.fields = [
                [
                    string_to_field_type[field]
                    for field in row
                ]
                for row in grid_config
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

    def get_empty_fields(self):
        empty_fields = []
        for r, row in enumerate(self.fields):
            for f, field in enumerate(row):
                if field == FieldType.EMPTY:
                    empty_fields.append(Field(x=f, y=r))
        return empty_fields

    def get_empty_cell_count(self):
        return len(self.get_empty_fields())

    def is_valid_move(self, field):
        return self.fields[field.y][field.x] == FieldType.EMPTY

    def to_string_lists(self):
        return [
            [
                field_type_to_string[field]
                for field in row
            ]
            for row in self.fields
        ]

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


class GridFieldEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, FieldType):
            map_to_json = dict(zip(['EMPTY', 'X', 'O'], ["", 'X', 'O']))
            return map_to_json[obj.name]
        return json.JSONEncoder.default(self, obj)
