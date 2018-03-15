from pytictactoe.field import Field
from pytictactoe.field_type import FieldType
from pytictactoe.grid import Grid


def test_empty_fields_all():
    grid = Grid()
    empty_fields = grid.get_empty_fields()
    assert len(empty_fields) == 9


def test_empty_fields():
    grid = Grid()
    field = Field(x=0, y=0)
    grid.set_field(field=field, field_type=FieldType.X)
    empty_fields = grid.get_empty_fields()
    assert len(empty_fields) == 8
