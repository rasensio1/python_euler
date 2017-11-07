#Multiples of 3 and 5

# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get
# 3, 5, 6 and 9. The sum of these multiples is 23.

# Find the sum of all the multiples of 3 or 5 below 1000.

import cProfile

def multiple_loop():
    accum = 0
    for i in xrange(0, 1000):
        if i % 3 == 0 or i % 5 == 0:
            accum += i

    return accum


def multiple_set():
    range_3 = xrange(0, 1000, 3)
    range_5 = xrange(0, 1000, 5)
    return sum(set(range_3).union(range_5))

def test_func(func, n):
    for _ in xrange(n):
        func()

cProfile.run("test_func(multiple_loop, 10000)") # 5x slower than using set
cProfile.run("test_func(multiple_set, 10000)") # fastest solution
