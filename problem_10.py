# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.

def primes_sieve():
    leng = 2000000
    seive = [True] * leng
    i = 2
    agg = 0
    while i < leng: 
        if seive[i] == True:
            agg += i
            seive[i*2::i] = [False] * (((leng-1)/i) - 1)
        i+=1
    print agg

primes_sieve()

