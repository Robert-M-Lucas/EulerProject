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


def get_largest(start, move, done):
    curr_largest = 0

    x, y = start
    dx, dy = move
    while True:
        try:
            grid[x][y]
        except IndexError:
            break
        try:
            to_product = ((x, y), (x - dx, y - dy), (x - 2 * dx, y - 2 * dy), (x - 3 * dx, y - 3 * dy))
            num = 1
            for i in to_product:
                if i[0] < 0 or i[1] < 0:
                    raise IndexError
                num *= grid[i[0]][i[1]]
                done[i[0]][i[1]] += 1

            if num > curr_largest:
                curr_largest = num
        except IndexError:
            pass
        x += dx
        y += dy

    return curr_largest


loc = ""

print("Column")
done = [[0 for _ in range(len(grid))] for __ in range(len(grid))]
for y in range(len(grid[0])):
    large = get_largest((0, y), (1, 0), done)
    if large > largest:
        largest = large
        loc = "col" + str(y)

print("Row")
for x in range(len(grid)):
    large = get_largest((x, 0), (0, 1), done)
    if large > largest:
        largest = large
        loc = "row"

print("Diag 1")
for y in range(len(grid[0])):
    large = get_largest((0, y), (1, 1), done)
    if large > largest:
        largest = large
        loc = "diag 1"

for x in range(len(grid)):
    large = get_largest((x, 0), (1, 1), done)
    if large > largest:
        largest = large
        loc = "diag 1-2"

for i in done:
    print(i)
print("**")

print("Diag 2")
for y in range(len(grid[0])):
    large = get_largest((len(grid) - 1, y), (-1, -1), done)
    if large > largest:
        largest = large
        loc = "diag 2"

for x in range(len(grid)):
    large = get_largest((x, len(grid) - 1), (-1, -1), done)
    if large > largest:
        largest = large
        loc = "diag 22"

for y in range(len(grid[0])):
    large = get_largest((len(grid) - 1, y), (1, -1), done)
    if large > largest:
        largest = large
        loc = "diag 2"

for x in range(len(grid)):
    large = get_largest((x, len(grid) - 1), (-1, 1), done)
    if large > largest:
        largest = large
        loc = "diag 22"

for y in range(len(grid[0])):
    large = get_largest((len(grid) - 1, y), (-1, 1), done)
    if large > largest:
        largest = large
        loc = "diag 2"

for x in range(len(grid)):
    large = get_largest((x, len(grid) - 1), (1, -1), done)
    if large > largest:
        largest = large
        loc = "diag 22"

for y in range(len(grid[0])):
    large = get_largest((len(grid) - (y+1), len(grid)), (-1, -1), done)
    if large > largest:
        largest = large
        loc = "diag 2"

for x in range(len(grid)):
    large = get_largest((len(grid), len(grid) - (x+1)), (-1, -1), done)
    if large > largest:
        largest = large
        loc = "diag 22"

for i in done:
    print(i)
print(largest)
print(loc)
