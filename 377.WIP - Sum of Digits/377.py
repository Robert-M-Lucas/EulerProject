

S = 0


for i in range(1, 18):
    print(i)
    target = 13 ** i
    for x in range(10**(target+1)):
        string = str(x)
        if "0" in string:
            continue
        total = 0
        for n in string:
            total += int(n)
        if total == target:
            S += x

print(S)
