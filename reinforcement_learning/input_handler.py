import numpy as np
import itertools

from pytictactoe.field import Field
from pytictactoe.field_type import FieldType

nr_fields = 9
pos_empty_fields = 0 * nr_fields
pos_x_fields = 1 * nr_fields
pos_o_fields = 2 * nr_fields

input_size = 3 * nr_fields
output_size = nr_fields


def get_input_state(grid):
    input_state = np.zeros(input_size, dtype='float32')
    flatten_grid = list(itertools.chain.from_iterable(grid.get_rows()))
    for i, field in enumerate(flatten_grid):
        if field == FieldType.EMPTY:
            set_input_state_field(input_state=input_state, offset=pos_empty_fields, i=i)
        elif field == FieldType.X:
            set_input_state_field(input_state=input_state, offset=pos_x_fields, i=i)
        elif field == FieldType.O:
            set_input_state_field(input_state=input_state, offset=pos_o_fields, i=i)
    return input_state


def set_input_state_field(input_state, offset, i):
    input_state[offset + i] = 1.


def index_to_field(index):
    x = index % 3
    y = int(index / 3)
    return Field(x=x, y=y)
