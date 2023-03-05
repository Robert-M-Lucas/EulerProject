import sympy

# def generate_primes(start, end, prime_list):
#     if start == 1:
#         start += 1
#
#     for i in range(start, end):
#         is_prime = True
#         for prime in prime_list:
#             if i % prime == 0:
#                 is_prime = False
#                 break
#         if is_prime:
#             prime_list.append(i)

def get_combination(power: int):
    combinations = []

    bit_counter = 1  # start from 1 to not allow no numbers being replaced
    initial_string = "-" * power

    while len(bin(bit_counter)) - 2 <= len(initial_string):
        current_combination = ""
        for i, d in enumerate(initial_string):
            if i+2 >= len(bin(bit_counter)):
                current_combination += d
                continue
            if bin(bit_counter)[::-1][i] == "1":
                current_combination += "*"
            else:
                current_combination += d
        combinations.append(current_combination)

        bit_counter += 1
    return combinations


# def is_prime(num: int) -> bool:
#     return num in full_prime_list


def combination_to_size(i: int, c: str) -> int:
    size = 0

    num_str = str(i)
    for x in range(0, 10):
        full_str = ""
        j = 0
        for l in c:
            if l == "-":
                full_str += num_str[j]
                j += 1
            else:
                full_str += str(x)

        if x == 0 and full_str[0] == "0":
            continue

        if sympy.isprime(int(full_str)):
            size += 1
    return size


done = False
for current_power in range(5, 10):
    print(f"Power: {current_power}")

    # full_prime_list = []
#
    # print("Generating primes...")
    # generate_primes(1, int(10**current_power), full_prime_list)


    # Get every combination of numbers and numbers to be replaced
    combinations = get_combination(current_power)
    for j, combination in enumerate(combinations):
        print(f"Testing combination {j+1}/{len(combinations)}")
        blank_count = 0
        for l in combination:
            if l == "-":
                blank_count += 1

        for i in range(int(10 ** (blank_count - 1)), int(10 ** blank_count)):
            #print(combination_to_size(i, combination), combination, i)
            if combination_to_size(i, combination) == 9:
                print(combination, i)
                done = True
                break
        if done:
            break
    if done:
        break


