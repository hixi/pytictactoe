from enum import Enum

FieldType = Enum('FieldType', ['EMPTY', 'X', 'O'])


def get_opponent_field_type(player):
    if player.field_type == FieldType.O:
        return FieldType.X
    else:
        return FieldType.O