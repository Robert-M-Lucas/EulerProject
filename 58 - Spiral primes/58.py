import sympy

i = 1
prime_count = 0
total_count = 1

for x in range(1, 1_000_000_000):
    for y in range(4):
        i += x*2
        if sympy.isprime(i):
            prime_count += 1
        total_count += 1

    if prime_count / total_count < 0.1:
        print((x*2) + 1)
        break
