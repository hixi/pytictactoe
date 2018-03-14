import argparse

import matplotlib.pyplot as plt

from pytictactoe.tournament import Tournament
from pytictactoe.player.random_player import RandomPlayer
from reinforcment_learning.model import build_model
from reinforcment_learning.rl_player import RlPlayer


def run(log_dir, episodes, rounds):
    model_path = log_dir + '/rl_model_tictactoe.h5'
    model = build_model(model_path=model_path)
    rl_player = RlPlayer(model=model)
    random_player = RandomPlayer()
    tournament = Tournament(rounds=rounds)
    tournament.register_player(rl_player)
    tournament.register_player(random_player)
    won_player_1 = 0
    won_player_2 = 0
    remis = 0
    for e in range(episodes):
        tournament.play()
        rl_player.replay()
        won_player_1 += tournament.statistic['players'][0]
        won_player_2 += tournament.statistic['players'][1]
        remis += tournament.statistic['remis']
        print_stats(won_player_1, won_player_2, remis)

    model.save_weights(model_path)
    print_loss(rl_player.loss)


def print_stats(won_player_1, won_player_2, remis):
    difference = won_player_1 - won_player_2
    print('-' * 180)
    print("Difference: ", difference)
    print("Player 1: ", won_player_1)
    print("Player 2: ", won_player_2)
    print("Remis: ", remis)


def print_loss(player_loss):
    plt.figure()
    epochs = range(1, len(player_loss) + 1)
    plt.plot(epochs, player_loss)
    plt.plot()
    plt.show()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='SieberJassBot', )
    parser.add_argument('-l', '--log_dir', dest='log_dir', help='Tensorboard log directory')
    parser.add_argument('-e', '--nr_episodes', dest='nr_episodes', help='Number of episodes to play', type=int)
    parser.add_argument('-r', '--rounds', dest='rounds', help='Rounds to play of a tournament', type=int)
    parser.set_defaults(log_dir='/pytictactoe', nr_episodes=2, rounds=2000)
    args = parser.parse_args()
    run(log_dir=args.log_dir, episodes=args.nr_episodes, rounds=args.rounds)
