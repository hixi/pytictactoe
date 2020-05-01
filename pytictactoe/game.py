import logging
import random

from pytictactoe.game_state import GameState
from pytictactoe.grid import Grid

logger = logging.getLogger(__name__)


class Game:
    def __init__(self, players, grid=None):
        self.players = players
        if not grid:
            self.grid = Grid()
        else:
            self.grid = grid

    def next_move_human_vs_computer(self, move=None):
        empty_cells_count = self.grid.get_empty_cell_count()
        human_player_index = 0
        computer_player_index = 1
        if not move:
            player_index = computer_player_index
        else:
            player_index = human_player_index
        player = self.players[player_index]
        self.choose(player=player)
        if self.won(player=player) == GameState.WON:
            after_decision_information(player=player, game_state=GameState.WON, grid=self.grid)
            after_decision_information(player=self.players[(player_index + 1) % 2], game_state=GameState.LOST,
                                        grid=self.grid)
            return GameState.WON if player_index == human_player_index else GameState.LOST
        if empty_cells_count > 1:
            after_decision_information(player=player, game_state=GameState.ONGOING, grid=self.grid)
            if player_index == human_player_index:
                return self.next_move_human_vs_computer()
            return GameState.ONGOING
        return GameState.REMI
    
    def start(self):
        start_player = random.randint(0, 1)
        for i in range(9):
            player = self.players[(i + start_player) % 2]
            self.choose(player=player)
            if self.won(player=player) == GameState.WON:
                after_decision_information(player=player, game_state=GameState.WON, grid=self.grid)
                after_decision_information(player=self.players[(i + start_player + 1) % 2], game_state=GameState.LOST,
                                           grid=self.grid)
                return player
            if i < 8:
                after_decision_information(player=player, game_state=GameState.ONGOING, grid=self.grid)
        for player in self.players:
            after_decision_information(player=player, game_state=GameState.REMI, grid=self.grid)
        return None

    def choose(self, player):
        is_allowed_field = False
        generator = player.choose_field(grid=self.grid)
        chosen_field = next(generator)
        while not is_allowed_field:
            is_allowed_field = self.grid.set_field(field=chosen_field, field_type=player.field_type)
            field = generator.send(is_allowed_field)
            chosen_field = chosen_field if field is None else field
        return chosen_field

    def won(self, player):
        winning_states = [self.grid.get_rows(), self.grid.get_columns(), self.grid.get_diagonals()]
        for winning_state in winning_states:
            for w in winning_state:
                if all(entry == player.field_type for entry in w):
                    return GameState.WON
        return None


def after_decision_information(player, game_state, grid):
    player.after_decision(game_state=game_state, grid=grid)
