import pathlib
import json

from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route, Mount, WebSocketRoute
from starlette.staticfiles import StaticFiles

from . import views
from .game_store import create_game, get_game
from .resources import opponents, make_move
from pytictactoe.grid import Grid
from pytictactoe.game import Game, GameState



def choose_opponent(request):
    adversaries = opponents.copy()
    [
        a.update({'start': f"/api/game"}) for a in adversaries
    ]
    return JSONResponse(adversaries)


async def new_game(request):
    # todo: real init
    data = await request.json()
    username = data['username']
    adversary_id = data['adversary']
    config = {'adversary': adversary_id, 'grid': Grid().to_string_lists(), 'username': username, 'state': GameState.ONGOING.name}
    game_obj = create_game(config)
    res = {'game': game_obj, 'move': f'/api/game/{game_obj["uuid"]}/move'}
    return JSONResponse(res)


def game_state(request):
    game_uuid = request.path_params['id']
    game_obj = get_game(game_uuid)
    res = {'game': game_obj, 'move': f'/api/game/{game_obj["uuid"]}/move'}
    return JSONResponse(res)


async def make_user_move(request):
    game_uuid = request.path_params['id']
    game_obj = get_game(game_uuid)
    if game_obj['state'] != GameState.ONGOING.name:
        res = {'game': game_obj, 'move': f'/api/game/{game_obj["uuid"]}/move'}
        return JSONResponse(res)
    data = await request.json()
    move = data['move']
    make_move(game_obj, move)
    game_obj = get_game(game_uuid)
    res = {'game': game_obj, 'move': f'/api/game/{game_obj["uuid"]}/move'}
    return JSONResponse(res)


def user(request):
    username = request.path_params['username']
    return JSONResponse({'content': 'Hello, %s!' % username})


def startup():
    print('Ready to go')


STATIC_DIR = pathlib.Path('static')
STATIC_DIR.mkdir(exist_ok=True)

routes = [
    Route('/', views.homepage),
    Route('/api/adversaries', choose_opponent),
    Route('/api/game', new_game, methods=['POST', 'HEAD']),
    Route('/api/game/{id}', game_state),
    Route('/api/game/{id}/move', make_user_move, methods=['POST']),
    Mount('/static', StaticFiles(directory=str(STATIC_DIR))),
]

api = Starlette(debug=True, routes=routes, on_startup=[startup])
