from pytictactoe.field import Field
from pytictactoe.field_type import FieldType, get_opponent_field_type
from pytictactoe.player.base_player import BasePlayer


class CleverPlayer(BasePlayer):
    def get_str_player(self):
        if get_opponent_field_type(self) == FieldType.X:
            return 'X'
        elif get_opponent_field_type(self) == FieldType.O:
            return 'O'

    def choose_field(self, grid):
        grid_str = grid_to_list(grid)
        player_str = self.get_str_player()

        cost, move = next_move(list(grid_str), player_str)

        x = move % 3
        y = int(move / 3)

        allowed = False
        while not allowed:
            field = Field(x, y)
            allowed = yield field
            if allowed:
                yield None
            else:
                print("Try it again, field is already chosen.\n")


def grid_to_list(grid):
    grid_list = ''
    for y in range(0, 3):
        for x in range(0, 3):
            if grid.get_field(x, y) == FieldType.EMPTY:
                grid_list += '-'
            elif grid.get_field(x, y) == FieldType.O:
                grid_list += 'O'
            elif grid.get_field(x, y) == FieldType.X:
                grid_list += 'X'
            else:
                raise RuntimeError('Unkwon FieldType on Board')
    return grid_list


def is_win(board):
    for i in range(3):
        if len(set(board[i * 3:i * 3 + 3])) is 1 and board[i * 3] is not '-': return True
    for i in range(3):
        if (board[i] is board[i + 3]) and (board[i] is board[i + 6]) and board[i] is not '-':
            return True
    if board[0] is board[4] and board[4] is board[8] and board[4] is not '-':
        return True
    if board[2] is board[4] and board[4] is board[6] and board[4] is not '-':
        return True
    return False


def next_move(board, player):
    if len(set(board)) == 1: return 0, 4
    next_player = 'X' if player == 'O' else 'O'
    if is_win(board):
        if player is 'X':
            return -1, -1
        else:
            return 1, -1
    res_list = []  # list for appending the result
    c = board.count('-')
    if c is 0:
        return 0, -1
    _list = []  # list for storing the indexes where '-' appears
    for i in range(len(board)):
        if board[i] == '-':
            _list.append(i)
    for i in _list:
        board[i] = player
        ret, move = next_move(board, next_player)
        res_list.append(ret)
        board[i] = '-'
    if player is 'X':
        max_ele = max(res_list)
        return max_ele, _list[res_list.index(max_ele)]
    else:
        min_ele = min(res_list)
        return min_ele, _list[res_list.index(min_ele)]
