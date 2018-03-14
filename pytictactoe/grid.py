from pytictactoe.field import Field


class Grid:
    def __init__(self):
        self.fields = [
            [Field.EMPTY, Field.EMPTY, Field.EMPTY],
            [Field.EMPTY, Field.EMPTY, Field.EMPTY],
            [Field.EMPTY, Field.EMPTY, Field.EMPTY]
        ]