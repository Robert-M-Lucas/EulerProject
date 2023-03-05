gon = []
best = 0

arms = 5
total = 10


def recurse(prev, i=None):
    global arms
    global total

    if i is None: i = total

    if i == 0:
        inner(prev)
        return

    for x in range(i):
        new = prev.copy()
        new.append(x)
        recurse(new, i - 1)


def inner(path):
    global best
    global arms
    global total

    options = [i for i in range(1, total + 1)]

    _gon = []
    for p in path:
        _gon.append(options[p])
        options.pop(p)

    if _gon.index(10) >= 5:
        return

    if _gon[0] != min(_gon[:arms]):
        return

    sums = []
    for i in range(arms):
        sum2 = i + arms
        if sum2 >= total:
            sum2 -= arms
        sum3 = i + arms + 1
        if sum3 >= total:
            sum3 -= arms

        sums.append(_gon[i] +
                    _gon[sum2] +
                    _gon[sum3])

    if len(set(sums)) != 1:
        return

    string = ""
    for i in range(arms):
        sum2 = i + arms
        if sum2 >= total:
            sum2 -= arms
        sum3 = i + arms + 1
        if sum3 >= total:
            sum3 -= arms

        string += str(_gon[i])
        string += str(_gon[sum2])
        string += str(_gon[sum3])

    if len(string) != 16:
        return

    print(string)

    if int(string) > best:
        print("New best")
        best = int(string)


recurse([])
print(f"Best: {best}")
