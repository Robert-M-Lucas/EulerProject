digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

target = 1_000_000

index = 0


def recurse(depth, remaining: list, full: str):
    global index

    depth += 1

    if len(full) > 0:
        remaining.remove(full[-1])

    if len(remaining) == 0:
        index += 1
        if index == target:
            print(full)
        return

    for i in remaining:
        recurse(depth, remaining.copy(), full + i)


recurse(0, digits, "")
