"""
Sum of incomplete words = sum of all words - sum of complete words
given a letters and l length sum all words = a ** l

complete words = a ** (l - a)    * a * a-1 * a-2 * a-3... assuming last a characters are the complete word
                 [any word]      [complete word]

number of ways any word and complete word characters can be arranged = l * l-1 * l-2 ...
= l!
"""
import math

k = 8 # max alph size
n = 8 # max word length

S = 0

for a in range(1, k+1): # alph size
    for l in range(1, n+1): # word length
        sum_all_words = a**l
        if l < a: # word can't be complete if length doesnt allow
            S += sum_all_words
            continue
        else:
            # complete_words = a ** (l-a)
            # for x in range(l):
            #     complete_words *= a-x
            # complete_words *= math.factorial(l)
            # S += sum_all_words - complete_words
            incomplete_words = (math.factorial(l) / math.factorial(a))/(a**2)
            S += incomplete_words

print(S)

