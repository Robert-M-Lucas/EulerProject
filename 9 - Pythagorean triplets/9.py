import math

for a in range(1000):
    for b in range(1000):
        if a + b + math.sqrt((a**2)+(b**2)) == 1000:
            print(a * b * math.sqrt((a**2)+(b**2)))