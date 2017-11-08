# coding: utf-8
# A palindromic number reads the same both ways. The largest palindrome made from
# the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.
import cProfile
from profiling import test_func

def isPalindome(n):
    if str(n) == str(n)[::-1]:
        return True

def largestPalindromeRange():
    ans = max(i * j
            for i in range(100, 1000)
            for j in range(100, 1000)
            if str(i * j) == str(i * j)[ : : -1])
    return str(ans)


def largestPalindromeLoops():
    i = 999
    max_pal = 0
    while i > 100:
        j = 999
        while j > 100:
            num = i * j
            if num > max_pal and isPalindome(num):
                max_pal = num
            j-= 1
        i -=1
    return max_pal

#This is a bad solution. Takes up a ton of space, very slow
def largestPalindromeMatrix():
    a = np.array(xrange(0, 1000))
    b = a.copy()[:,None]
    res = a*b
    return max([num for num in res if isPalindome(num)])

cProfile.run("test_func(largestPalindromeLoops, 5)") #this is 5x faster
cProfile.run("test_func(largestPalindromeRange, 5)")
