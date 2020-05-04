from random import choice
from math import inf as infinity

from pytictactoe.player.base_player import BasePlayer
from pytictactoe.game import Game
from pytictactoe.field import Field
from pytictactoe.grid import Grid
from pytictactoe.field_type import FieldType


class MiniMaxPlayer(BasePlayer):
    def choose_field(self, grid):
        empty_cells = grid.get_empty_fields()
        depth = len(empty_cells)
 
        if depth == 9:
            x, y = choice([0, 1, 2]), choice([0, 1, 2])
        else:
            board = TicTacToeBoard(grid=grid.to_string_lists())
            move = minimax(board, self.field_type)
            x, y = move
        is_allowed = yield Field(y, x)
        if is_allowed:
            yield None


class TicTacToeBoard:
    def __init__(self, grid=None):
        # 3 possible states per board square
        # (i)   "" - blank square
        # (ii)  "X" - X  entry
        # (iii) "O" - O entry
        if not grid:
            self.board = [["" for col in range(3)] for row in range(3)]
        self.board = grid
        self.board_score = 0

    def execute_turn(self, symbol, row, col):
        # Checks if (row, col) in board is currently blank (0)
        # It then fills (row, col) in board with either a 1 (X)
        # OR a 2 (O)

        # Also updates the history variable with the possible
        # moves that can be executed

        # Returns True if executing the turn was successful
        # Returns False if executing the turn was unsuccessful
        if self.board[row][col] == 0:
            if symbol == 'X':
                self.board[row][col] = symbol
                return True
            elif symbol == 'O':
                self.board[row][col] = symbol
                return True
            return False
        return False

    def reset_board(self):
        for row in range(3):
            for col in range(3):
                self.board[row][col] = ""

    def game_is_won(self):
        for row in range(3):
            if self.board[row][0] == self.board[row][1] and self.board[row][1] == self.board[row][2] and self.board[row][0] != "":
                return True

        for col in range(3):
            if self.board[0][col] == self.board[1][col] and self.board[1][col] == self.board[2][col] and self.board[0][col] != "":
                return True

        if self.board[0][0] == self.board[1][1] and self.board[1][1] == self.board[2][2] and self.board[0][0] != "":
            return True

        if self.board[2][0] == self.board[1][1] and self.board[1][1] == self.board[0][2] and self.board[2][0] != "":
            return True

        return False

    def current_player(self):
        number_Xs = self.num_Xs(self.board)
        number_Os = self.num_Os(self.board)
        if number_Xs == number_Os: # If equal numbers of symbols, 'X' is current player
            return 'X'
        return 'O' # Otherwise 'O' is the current player

    def num_Xs(self, board):
        num_X = 0
        for row in range(3):
            for col in range(3):
                if self.board[row][col] == "X":
                    num_X+=1
        return num_X

    def num_Os(self, board):
        num_O = 0
        for row in range(3):
            for col in range(3):
                if self.board[row][col] == "O":
                    num_O+=1
        return num_O

    def num_open_spaces(self):
        blank_cells = 0
        for row in range(3):
            for col in range(3):
                if self.board[row][col] == "":
                    blank_cells+=1
        return blank_cells

    def get_possible_moves(self):
        # Returns all the possible moves current player can
        # make on this board
        # Returns: A list of tuples in the form (row, col)
        possible_moves = []
        for row in range(3):
            for col in range(3):
                if self.board[row][col] == "":
                    possible_moves.append((row,col))
        return possible_moves

    def make_move(self, current_player, row, col):
        board_copy = [element[:] for element in self.board]
        if current_player == 'X':
            board_copy[row][col] = "X"
        else:
            board_copy[row][col] = "O"
        copy_board = TicTacToeBoard()
        copy_board.board = board_copy
        return copy_board

    def calculate_board_score(self):
        # Calculates the score of the current board, there are 3 main scenarios:
        # (i) If 'X' wins => returns 10
        # (ii) If 'O' wins => returns -10
        # (iii) No one wins => returns 0
        for row in range(3):
            if self.board[row][0] == self.board[row][1] and self.board[row][1] == self.board[row][2] and self.board[row][0] != 0:
                if self.board[row][0] == "X":
                    return 10
                elif self.board[row][0] == "O":
                    return -10

        for col in range(3):
            if self.board[0][col] == self.board[1][col] and self.board[1][col] == self.board[2][col] and self.board[0][col] != 0:
                if self.board[0][col] == "X":
                    return 10
                elif self.board[0][col] == "O":
                    return -10

        if self.board[0][0] == self.board[1][1] and self.board[1][1] == self.board[2][2] and self.board[0][0] != 0:
            if self.board[0][0] == "X":
                return 10
            elif self.board[0][0] == "O":
                return -10

        if self.board[2][0] == self.board[1][1] and self.board[1][1] == self.board[0][2] and self.board[2][0] != 0:
            if self.board[2][0] == "X":
                return 10
            elif self.board[2][0] == "O":
                return -10

        return 0



# Minimax function we will call when the 'Hard' AI player 
# is chosen.
def minimax(board, player):
    best_score = float('inf')
    best_move = None
    if player == 'X':
        best_score = float('-inf')
    for possible_move in board.get_possible_moves():
        current_row, current_col = possible_move
        new_board = board.make_move(player, current_row, current_col)
        print(new_board.board)
        if player == 'X':
            score = minimizer(new_board)
            if score > best_score:
                best_score = score
                best_move = (current_row, current_col)
        else:
            score = maximizer(new_board)
            print(score)
            if score < best_score:
                best_score = score
                best_move = (current_row, current_col)
            print("")
 
    return best_move


def minimizer(board):
    # Current player is assumed to be 'O' here
    current_score = board.calculate_board_score()
    if current_score != 0 or board.num_open_spaces() == 0:
        return current_score 
    average_score = 0.0
    for possible_move in board.get_possible_moves():
        current_row, current_col = possible_move
        new_board = board.make_move('O', current_row, current_col)
        score = maximizer(new_board)
        #print("Maximizer Score = " + str(score))
        #lowest_score = min(lowest_score, score)
        average_score+=score
    return average_score/len(board.get_possible_moves())


def maximizer(board):
    # Current player is assumed to be 'X' here
    current_score = board.calculate_board_score()
    if current_score != 0 or board.num_open_spaces() == 0:
        return current_score 
    highest_score = float("-inf")
    for possible_move in board.get_possible_moves():
        current_row, current_col = possible_move
        new_board = board.make_move('X', current_row, current_col)
        score = minimizer(new_board)
        #print("Minimizer Score = " + str(score))
        highest_score = max(highest_score, score)
    return highest_score
