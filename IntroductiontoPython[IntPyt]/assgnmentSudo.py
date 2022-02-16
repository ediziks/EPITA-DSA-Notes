table = [
    [7, 9, 1, 2, 6, 5, 4, 8, 3],
    [6, 2, 5, 8, 4, 3, 7, 9, 1],
    [4, 8, 3, 9, 7, 1, 6, 2, 5],
    [8, 1, 4, 5, 9, 7, 2, 3, 6],
    [2, 3, 6, 1, 8, 4, 9, 5, 7],
    [9, 5, 7, 3, 2, 6, 8, 1, 4],
    [5, 6, 9, 4, 3, 2, 1, 7, 8],
    [3, 4, 2, 7, 1, 8, 5, 6, 9],
    [1, 7, 8, 6, 5, 9, 3, 4, 2],
]


def correct(sudo, row, col, int):
    for i in range(9):
        if sudo[row][i] == int:
            return False

    for i in range(9):
        if sudo[i][col] == int:
            return False

    horizon = row - row % 3
    vertical = col - col % 3

    for i in range(horizon, horizon + 3):
        for j in range(vertical, vertical + 3):
            if sudo[i][j] == int:
                return False

    return True


def calc(sudo):
    for i in range(9):
        for j in range(9):
            if sudo[i][j] == 0:
                for int in range(1, 10):
                    if correct(sudo, i, j, int):
                        sudo[i][j] = int
                        result = calc(sudo)
                        if result == True:
                            return True
                        else:
                            sudo[i][j] = 0
                return False
    return True


calc(table)
for i in table:
    print(i)
