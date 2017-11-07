# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?


def largest_prime(n):
    i = 1
    factor_me = n
    biggest_prime = 1

    while i <= factor_me:
        if factor_me % i == 0:
           biggest_prime = i 
           factor_me /= i
        i+=1
    return biggest_prime

print largest_prime(600851475143)
