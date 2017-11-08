# Find the difference between the sum of the squares of the first one hundred
# natural numbers and the square of the sum.

def sum_squares_upto(n):
    return reduce((lambda x, y: y**2 + x), xrange(1, n + 1))

def square_sum_upto(n):
    return ((n**2 + n)/2)**2

def difference(n):
    return square_sum_upto(n) - sum_squares_upto(n)


print difference(100)

