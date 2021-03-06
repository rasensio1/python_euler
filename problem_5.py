# 2520 is the smallest number that can be divided by each of the numbers from 1 to
# 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the
# numbers from 1 to 20?
import cProfile
from helpers import profiling


#Least common multiple of x and y is (x*y)/greatest_common_denom(x, y)
def gcd(x, y):
    for i in xrange(min(max(x, y)/2, min(x, y)), 0, -1):
        if x % i == 0 and y % i == 0:
            return i


def smallest_multiple():
    nums = set(range(12, 21))
    agg = 11
    for num in nums:
        agg = ((agg * num) / gcd(agg, num))

    return agg

print smallest_multiple()

cProfile.run("profiling.test_func(smallest_multiple, 1000)") #this is super fast!
