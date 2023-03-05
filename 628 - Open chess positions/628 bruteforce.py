import sys
import threading

sys.setrecursionlimit(10**8)


def f(size):
    path = [i for i in range(size)]
    return get_pawns([], size)


def get_pawns(prev, i):
    if i == 0:
        return f2(path_to_board(prev))

    total = 0

    for x in range(i):
        if len(prev) == 1: print(x)
        new = prev.copy()
        new.append(x)
        total += get_pawns(new, i - 1)

    return total


def path_to_board(prev):
    options = [i for i in range(len(prev))]
    board = [[False for _ in range(len(prev))] for _ in range(len(prev))]

    for i, p in enumerate(prev):
        board[i][options[p]] = True
        options.pop(p)

    return board


def f2(board):
    if board[0][0] or board[len(board) - 1][len(board) - 1]:
        return 0

    if ant(board, (0, 0)):
        [print(i) for i in board]
        print()
        return 1
    return 0


def ant(board, pos):
    if board[pos[0]][pos[1]]:
        return False

    if pos[0] == len(board) - 1 and pos[1] == len(board) - 1:
        return True

    if pos[1] + 1 < len(board) and ant(board, (pos[0], pos[1] + 1)):
        return True

    if pos[0] + 1 < len(board) and ant(board, (pos[0] + 1, pos[1])):
        return True
    return False


def compute():
    print(f(10 ** 8) % 1_008_691_207)


threading.stack_size(200000000)
threading.Thread(target=compute).start()
