import random
from functools import partial
from pathlib import Path

from pytictactoe.field import Field
from pytictactoe.field_type import FieldType
from pytictactoe.player.base_player import BasePlayer
from reinforcement_learning.rl_player import RlPlayer
from pytictactoe.player.defensive_player import DefensivePlayer
from pytictactoe.player.clever_player import CleverPlayer
from pytictactoe.player.web_player import WebAPIPlayer
from pytictactoe.tournament import Tournament
from pytictactoe.game import Game
from pytictactoe.grid import Grid

from .game_store import create_game, get_game, update_game


class RandomPlayer(BasePlayer):
    def choose_field(self, grid):
        allowed = False
        while not allowed:
            field = Field(x=random.randint(0, 2), y=random.randint(0, 2))
            allowed = yield field
            if allowed:
                yield None

RL_WEIGHTS_PATH = Path(__file__).parent.parent / 'reinforcement_learning/weights'

string_to_opponent = {
    'random-player': RandomPlayer,
    'reinformcent-learning-player': partial(
        RlPlayer, 
        model_path=(RL_WEIGHTS_PATH / 'rl_model_tictactoe.h5').absolute(),
    ),
    'defensive-player': DefensivePlayer,
    'clever-player': CleverPlayer,
}


opponents = [
    {
        'name': 'Random Player (Dummy)',
        'id': 'random-player',
        'description': 'very easy',
    },
    {
        'name': 'Reinforcement Learning Player',
        'id': 'reinformcent-learning-player',
        'description': 'still learning',
    },
    {
        'name': 'Defensive Player',
        'id': 'defensive-player',
        'description': 'defensive strategy',
    },
    {
        'name': 'Clever Player',
        'id': 'clever-player',
        'description': 'clever strategy',
    },
]

def get_players(player_move, chosen_adversary_id):
    web_player = WebAPIPlayer(player_move)
    web_player.field_type = FieldType.X
    adversary = string_to_opponent[chosen_adversary_id]()
    adversary.field_type = FieldType.O
    players = {'human': web_player, 'adversary': adversary}
    return [players['human'], players['adversary']]


def get_game_instance(game_config, player_move):
    grid = Grid(grid_config=game_config['grid'])
    players = get_players(player_move, game_config['adversary'])
    game = Game(players=players, grid=grid)
    return game


def make_move(game_config, player_move):
    game = get_game_instance(game_config, player_move)
    state = game.next_move_human_vs_computer(player_move)
    update_game(game_config['uuid'], grid=game.grid.to_string_lists(), state=state.name)
    return game.grid
