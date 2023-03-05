def get_rotations(num):
    out = [num]
    num = str(num)
    for _ in range(len(num) - 1):
        num = num[-1] + num[:-1]
        if int(num) not in out:
            out.append(int(num))
    return out


primes = []
count = 0

for x in range(2, 1_000_001):
    if x % 1000 == 0:
        print(x / 10000, "%")

    isPrime = True

    for p in primes:
        if x % p == 0:
            isPrime = False
            break

    if isPrime:
        primes.append(x)

        is_rotational = True
        rotations = get_rotations(x)
        if x != max(rotations):
            continue

        for r in rotations:
            if r not in primes:
                is_rotational = False
                break

        if is_rotational:
            count += len(rotations)

print(count)
input()
