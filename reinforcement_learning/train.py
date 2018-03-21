import os
import argparse

import matplotlib.pyplot as plt

from pytictactoe.tournament import Tournament
from pytictactoe.player.random_player import RandomPlayer
from pytictactoe.player.defensive_player import DefensivePlayer
from pytictactoe.player.clever_player import CleverPlayer
from reinforcement_learning.rl_player import RlPlayer


def run(log_dir, episodes, rounds):
    model_path = log_dir + '/rl_model_tictactoe.h5'
    rl_player = RlPlayer(model_path=model_path, rounds=rounds)
    opponent = RandomPlayer()
    # opponent = DefensivePlayer()
    # dopponent = CleverPlayer()
    # opponent = RlPlayer(model_path=log_dir + '/rl_model_tictactoe_good.h5')
    tournament = Tournament(rounds=rounds)
    tournament.register_player(rl_player)
    tournament.register_player(opponent)
    won1 = []
    won2 = []
    remis = []
    for e in range(episodes):
        tournament.play()
        rl_player.replay()
        won1.append(tournament.statistic['players'][0])
        won2.append(tournament.statistic['players'][1])
        remis.append(tournament.statistic['remis'])
        print_stats(tournament.statistic['players'][0], tournament.statistic['players'][1],
                    tournament.statistic['remis'], rounds)
        rl_player.model.save_weights(model_path)
    print_diffs(won1, won2, remis)


def print_stats(won_player_1, won_player_2, remis, rounds):
    difference = won_player_1 - won_player_2
    print('-' * 180)
    print("Difference: {0} ".format(difference))
    print("Player 1: {0} / {1}".format(won_player_1, rounds))
    print("Player 2: {0} / {1}".format(won_player_2, rounds))
    print("Remis: ", remis)


def print_diffs(won1, won2, remis):
    plt.figure()
    epochs = range(1, len(won1) + 1)
    plt.plot(epochs, won1)
    plt.plot(epochs, won2)
    plt.plot(epochs, remis)
    plt.legend(['Player 1', 'Player 2', 'Remis'], loc='upper left')
    plt.show()


if __name__ == "__main__":
    dir_path = os.path.dirname(os.path.realpath(__file__))
    parser = argparse.ArgumentParser(description='Tic-Tac-Toe Bot', )
    parser.add_argument('-l', '--log_dir', dest='log_dir', help='Tensorboard log directory')
    parser.add_argument('-e', '--nr_episodes', dest='nr_episodes', help='Number of episodes to play', type=int)
    parser.add_argument('-r', '--rounds', dest='rounds', help='Rounds to play of a tournament', type=int)
    parser.set_defaults(log_dir=dir_path + '/weights', nr_episodes=10, rounds=1000)
    args = parser.parse_args()
    run(log_dir=args.log_dir, episodes=args.nr_episodes, rounds=args.rounds)
