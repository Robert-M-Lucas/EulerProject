import math


def fct(x): return math.factorial(x)


size = 10**8

all_possible = fct(size)

blocked = 0
for length in range(1, size):
    blocked += 2 * fct(size - length)

    for width in range(1, (size - length) + 1):
        blocked -= fct((size - length) - width)

blocked += 1

print(f"Size: {size}")
print(f"Possible: {all_possible}, Blocked: {blocked}") #, Collisions: {collisions}")
print("-----")
print((all_possible - blocked) % 1_008_691_207)

"""
11
12
21
22
"""