with open("grid.txt", "r") as f:
    data = f.read()

grid_str = [i for i in [j.split(" ") for j in data.split("\n")]]

grid = []
for y in grid_str:
    new_line = []
    for x in y:
        new_line.append(int(x))
    grid.append(new_line)

largest = 0


def get_largest(start, move):
    curr_largest = 0

    x, y = start
    dx, dy = move
    while True:
        try:
            grid[x][y]
        except IndexError:
            break
        try:
            num = grid[x][y] * grid[x - dx][y - dy] * grid[x - 2 * dx][y - 2 * dy] * grid[x - 3 * dx][y - 3 * dy]
            if num > curr_largest:
                curr_largest = num
        except IndexError:
            pass
        x += dx
        y += dy
    return curr_largest

print("Row")
for y in range(len(grid[0])):
    large = get_largest((0, y), (1, 0))
    if large > largest:
        largest = large

print("Column")
for x in range(len(grid)):
    large = get_largest((x, 0), (0, 1))
    if large > largest:
        largest = large

print("Diag 1")
for y in range(len(grid[0])):
    large = get_largest((0, y), (1, 1))
    if large > largest:
        largest = large

for x in range(len(grid)):
    large = get_largest((x, 0), (1, 1))
    if large > largest:
        largest = large

print("Diag 2")
for y in range(len(grid[0])):
    large = get_largest((len(grid)-1, y), (1, 1))
    if large > largest:
        largest = large

for x in range(len(grid)):
    large = get_largest((x, len(grid)-1), (1, 1))
    if large > largest:
        largest = large

print(largest)
