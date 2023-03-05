from math import factorial
import sys

n = 200_000
n_fact = factorial(n)

target = 10 ** 12

total = 0

def factorial_range(a, b):
    x = b
    for i in range(a, b):
        x *= i
    return x


def coefs(r, k):
    global n_fact
    global n
    # return n_fact / (factorial(n - r) * factorial(r - k) * factorial(k))
    return factorial_range(n-r, n) // (factorial(r - k) * factorial(k))


for r in range(n + 1):
    if r % 10 == 0:
        print(f"{(round(r / n) * 100, 3)}%")

    for k in range(int(r / 2)):
        c = coefs(r, k)
        if c % target == 0:
            total += 2

    if r / 2 != int(r / 2):
        c = coefs(r, int(r / 2) + 1)
        if c % target == 0:
            total += 1
