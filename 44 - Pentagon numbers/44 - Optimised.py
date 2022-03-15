import sys

all_pents = []
open_set = []

for n in range(1, 1_000_000_000):
    if n % 1000 == 0:
        print(n)

    p = (n*((3*n)-1))/2

    new_op = []
    for op in open_set:
        if p == op[2]:
            print(op, op[0] - op[1])
            sys.exit(1)
            break
        elif p < op[2]:
            new_op.append(op)
    open_set = new_op

    for prv_p in all_pents:
        if p - prv_p in all_pents:
            open_set.append([p, prv_p, p + prv_p])

    all_pents.append(p)

# [7042750.0, 1560090.0, 8602840.0] 5482660.0
