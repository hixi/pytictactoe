import logging

from pytictactoe.field_type import FieldType
from pytictactoe.game import Game

logger = logging.getLogger(__name__)


class Tournament:
    def __init__(self, rounds=5):
        self.rounds = rounds
        self.players = []
        self.games = []
        self.statistic = dict(players=[0, 0], remis=0)

    def register_player(self, player):
        assert len(self.players) < 2
        player.field_type = self._get_field_type()
        self.players.append(player)

    def _get_field_type(self):
        return FieldType.O if len(self.players) else FieldType.X

    def play(self):
        logger.info('Tournament starts, there are {} rounds to play.'.format(self.rounds))
        for i in range(self.rounds):
            game = Game(players=self.players)
            self.games.append(game)
            logger.info('-' * 200)
            logger.info('Round {} starts.'.format(len(self.games)))
            logger.info('-' * 200)
            winner = game.start()
            self.update_statistic(winner)
            logger.info('\nRound {} is over.'.format(len(self.games)))
            logger.info('Points: Player 1: {0} , Player 2: {1}, Remis: {2}. \n'.format(self.statistic['players'][0],
                                                                                       self.statistic['players'][1],
                                                                                       self.statistic['remis']))
        logger.info('{0} won! \n'.format(self.tournament_winner()))
        self.reset()

    def update_statistic(self, winner):
        if winner is None:
            self.statistic['remis'] += 1
        else:
            self.statistic['players'][self.players.index(winner)] += 1

    def tournament_winner(self):
        return self.players[self.statistic['players'].index(max(self.statistic['players']))]

    def reset(self):
        self.games = []
