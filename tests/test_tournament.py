from pytictactoe.player.random_player import RandomPlayer
from pytictactoe.tournament import Tournament


def test_tournamet():
    tournament = Tournament(rounds=1)
    tournament.register_player(RandomPlayer())
    tournament.register_player(RandomPlayer())
    tournament.play()
    player_1 = tournament.statistic['players'][0]
    player_2 = tournament.statistic['players'][1]
    remis = tournament.statistic['remis']
    assert sum([player_1, player_2, remis]) == 1
