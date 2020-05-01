import pathlib
import json
from uuid import uuid4

TMP_STORE_FOLDER = pathlib.Path('/tmp/')


def get_game_filepath(uuid):
    return TMP_STORE_FOLDER / f"{str(uuid)}.json"


def create_game(settings):
    uuid = uuid4().hex
    game_data_file = get_game_filepath(uuid)
    while game_data_file.exists():
        uuid = uuid4().hex
        game_data_file = get_game_filepath(uuid)
    settings['uuid'] = uuid
    with open(game_data_file, 'w') as json_file:
        json_file.write(json.dumps(settings))
    return settings


def get_game(uuid):
    game_config = TMP_STORE_FOLDER / f"{str(uuid)}.json"
    with game_config.open('r') as json_file:
        json_result = json.loads(json_file.read())
    return json_result


def update_game(uuid, grid, state):
    game_data = get_game(uuid)
    # record history
    if game_data.get('grid'):
        if not game_data.get('grid_history'):
            game_data['grid_history'] = []
        game_data['grid_history'].append({'grid': grid, 'state': state})
    # set new state
    game_data['grid'] = grid
    game_data['state'] = state
    game_data_file = get_game_filepath(uuid)
    with open(game_data_file, 'w') as json_file:
        json_file.write(json.dumps(game_data))
    return game_data
