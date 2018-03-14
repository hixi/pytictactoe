import logging

from pytictactoe.grid import Grid

logger = logging.getLogger(__name__)


class Game:
    def __init__(self):
        self.players = []
        self.grid = Grid()

    def register(self, player):
        self.players.append(player)
        assert len(self.players) <= 2

    def start(self):
        start_player_index = 0
        has_won = False
        while not has_won:
            player = self.players[start_player_index % 2]
            self.choose(player=player)
            has_won = self.won(player=player)

    def choose(self, player):
        is_allowed_field = False
        generator = player.choose_field(grid=self.grid)
        chosen_field = next(generator)
        while not is_allowed_field:
            is_allowed_card = self.grid.set_field(field=chosen_field, field_type=player.field_type)
            field = generator.send(is_allowed_card)
            chosen_field = chosen_field if field is None else field
        else:
            logger.info('{0}:({1}/{2})'.format(player, chosen_field.x, chosen_field.y))
        return chosen_field

    def won(self, player):
        winning_states = [self.grid.get_rows(), self.grid.get_columns(), self.grid.get_diagonals()]
        for winning_state in winning_states:
            for w in winning_state:
                if all(entry == player.field_type for entry in w):
                    return True
        return False
