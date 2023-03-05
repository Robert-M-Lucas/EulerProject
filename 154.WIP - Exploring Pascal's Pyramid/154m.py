from math import factorial
import sys

id, l, h = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
print(id, "starting from", l, "to", h)

n = 200_000


# def factorial_range(a, b):
#     x = b
#     for i in range(a, b):
#         x *= i
#     return x


def two_five_factorial(a, b):
    x = 1
    steps = [2, 1, 1, 2, 2, 2]
    i = a
    while i <= b:
        for z in steps:
            x *= i
            i += z
            if i > b:
                break

    return x


def coefs(r, k):
    global n_fact
    global n

    if r < (n / 2):
        return two_five_factorial(n - r, n) // (two_five_factorial(2, r - k) * two_five_factorial(2, k))
    else:
        return n_fact // (two_five_factorial(2, n - r) * two_five_factorial(2, r - k) * two_five_factorial(2, k))


n_fact = two_five_factorial(2, n)

target = 10 ** 12

total = 0


for r in range(l, h):
    if r % 10 == 0:
        print(f"{id} - {round(((r - l) / (h - l)) * 100, 3)}%")

    for k in range(int(r / 2)):
        c = coefs(r, k)
        if c % target == 0:
            total += 2

    if r / 2 != int(r / 2):
        c = coefs(r, int(r / 2) + 1)
        if c % target == 0:
            total += 1

print(total)
with open(f"{id}.txt", "w") as f:
    f.write(str(total))