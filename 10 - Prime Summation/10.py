import sympy

x = 0
for i in range(2_000_000):
    if sympy.isprime(i):
        x += i
print(x)
