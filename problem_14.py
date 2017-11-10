# coding: utf-8
# The following iterative sequence is defined for the set of positive integers:

#     n → n/2 (n is even)
#     n → 3n + 1 (n is odd)

# Using the rule above and starting with 13, we generate the following
# sequence:
#     13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

# It can be seen that this sequence (starting at 13 and finishing at 1) contains
# 10 terms. Although it has not been proved yet (Collatz Problem), it is thought
# that all starting numbers finish at 1.

# Which starting number, under one million, produces the longest chain?

# NOTE: Once the chain starts the terms are allowed to go above one million.

import cProfile

def max_col_len(n):
    max_so_far = 0
    bingo = 0
    i = 1
    memo = {1: 1}
    while i < n:
        start = i
        count = 1
        while True:
            if start in memo:
                count += memo[start]
                memo[i] = count
                break
            if start % 2 == 0:
                start /= 2
            else:
                start = 3 * start + 1
            count += 1

        if count > max_so_far:
            max_so_far = count
            bingo = i
        i+=2

    print bingo

cProfile.run("max_col_len(1e6)") #2s
