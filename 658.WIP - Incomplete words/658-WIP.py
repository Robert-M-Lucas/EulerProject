"""
For words shorter than len(a) [l]
l + l^2 + l^3 ... l^(l-1)
For words >= l and words < n
... + (n*n-1*n-3*n-4) + (n*n-1*n-3*n-4*n-5)
"""

l = 5
n = 7
total = 0
for i in range(n+1):
    if i < l:
        total += l**i
    else:
        sub_tot = n
