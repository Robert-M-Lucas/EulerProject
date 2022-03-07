max_num = 4_000_000

prev_num = 1
num = 1

total = 0

while num < max_num:
    if num % 2 == 0:
        total += num

    temp_num = num
    num += prev_num
    prev_num = temp_num

print(total)
