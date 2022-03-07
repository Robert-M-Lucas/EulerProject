"""
For every prime with n digits the highest number replacements can give is 9xn
e.g. 1031 -> 9999 if every number is replaced

find primes -> 10
test primes 1 -> 10
find primes -> 100
test primes 10 -> 100
etc
"""


def generate_primes(start, end, prime_list=[]) -> list:
    if start == 1:
        start += 1

    current_primes = []
    for i in range(start, end):
        is_prime = True
        for prime in prime_list:
            if i % prime == 0:
                is_prime = False
                break
        if is_prime:
            prime_list.append(i)
            current_primes.append(i)
    return current_primes


def get_combinations(number) -> str:
    number = str(number)

    combinations = []

    # Will iterate through all combinations of digits and replaced digits e.g. 1031 and b'1001' -> *03*
    byte_counter = 1
    while len(bin(byte_counter)) - 2 <= len(number):
        current_combination = ""
        for i, d in enumerate(number):
            if i+2 >= len(bin(byte_counter)):
                current_combination += d
                continue
            if bin(byte_counter)[::-1][i] == "1":
                current_combination += "*"
            else:
                current_combination += d
        combinations.append(current_combination)

        byte_counter += 1
    return combinations


def get_prime_family_size(combination_str: str, prime_list: list) -> int:
    size = 0
    for i in range(10):
        num_str = ""
        for d in combination_str:
            if d != "*":
                num_str += d
            else:
                num_str += str(i)

        if int(num_str) in prime_list:
            size += 1
    return size


target_family_size = 8

full_prime_list = []
current_pow = 1

greatest_size = 0

while True:
    print(f"10^{current_pow} - getting primes")
    current_primes = generate_primes(0, 10 ** current_pow, full_prime_list)
    print("Testing primes")
    for prime in current_primes:
        for combination in get_combinations(prime):
            family_size = get_prime_family_size(combination, full_prime_list)
            if family_size == target_family_size:
                print(prime, combination)
            if family_size > greatest_size:
                greatest_size = family_size
                print(f"New greatest family size {greatest_size} created by {prime}, {combination}")

    current_pow += 1
