import pytest

from pytictactoe.field import Field
from reinforcement_learning.input_handler import index_to_field


@pytest.mark.parametrize("index, field,", [
    (0, Field(x=0, y=0)),
    (1, Field(x=1, y=0)),
    (2, Field(x=2, y=0)),
    (3, Field(x=0, y=1)),
    (4, Field(x=1, y=1)),
    (5, Field(x=2, y=1)),
    (6, Field(x=0, y=2)),
    (7, Field(x=1, y=2)),
    (8, Field(x=2, y=2)),
])
def test_index_to_field(index, field):
    assert index_to_field(index) == field
