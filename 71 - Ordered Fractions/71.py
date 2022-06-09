
fracts = []

print("Generating")
for d in range(1, 1_000_000):
    if d % 1000 == 0:
        print(round((d*100) / 1_000_000, 2))
    for n in range(1, d):
        if d % n == 0:
            continue
        fracts.append((n, d, n/d))

print("Sorting")
fracts_sorted = sorted(fracts, key=lambda x: x[2])

print(fracts_sorted[0])

print("Indexing")

