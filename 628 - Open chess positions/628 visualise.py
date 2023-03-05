count = 0
def f(size):
    return get_pawns([], size)


def get_pawns(prev, i):
    if i == 0:
        print_board(path_to_board(prev))

    for x in range(i):
        new = prev.copy()
        new.append(x)
        get_pawns(new, i - 1)


def path_to_board(prev):
    options = [i for i in range(len(prev))]
    board = [[False for _ in range(len(prev))] for _ in range(len(prev))]

    for i, p in enumerate(prev):
        board[i][options[p]] = True
        options.pop(p)

    return board

def print_board(board):
    global count
    string = ""
    for i in board:
        string += "|"
        for c in i:
            if c:
                string += "X"
            else:
                string += " "
            string += " "
        string += "|\n"
    print(string + "-------------")
    # if input("") != "":
    #     count += 1


f(5)
print(count)