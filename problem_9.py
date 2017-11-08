# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a2 + b2 = c2

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.
import cProfile
from helpers import profiling

def triplet_product():
    max_val = 1000
    i = 1
    while i < max_val/3:
        for k in xrange(i + 1, 2 * (max_val/3)):
            if i**2 + k**2 == (max_val - i - k)**2:
                return i*k*(max_val - (i +k))
        i += 1

print triplet_product()

cProfile.run("profiling.test_func(triplet_product, 10)")
