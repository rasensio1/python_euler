# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that
# the 6th prime is 13.

# What is the 10 001st prime number?
import cProfile

def primes(n):
    primes = [2]
    count = 1
    i = 1
    while count < n:
        i+=2
        if not any([i % num == 0 for num in primes]):
            primes.append(i)
            count += 1

    print i

def primes_sieve(n):
    leng = 1000000
    seive = [True] * leng
    i = 2
    count = 0
    while count < n: 
        if seive[i] == True:
            count += 1
            seive[i*2::i] = [False] * (((leng-1)/i) - 1)
        i+=1
    print i
    


# cProfile.run("primes(10001)") #slow! 25s
cProfile.run("primes_sieve(10001)") #fast! 
