from test_framework import generic_test
import math

def is_prime(n):

    if n < 2:
        return False

    if n == 2:
        return True

    ip = True
    # could be improced by using sqrt(n) instead
    for i in range(2, n):
        if n % i == 0:
            ip = False
            break

    return ip

def bf(n):

    primes = []

    for i in range(2, n + 1):
        if is_prime(i):
            primes.append(i)

    return primes

def first(n):

    if n <= 1:
        return []

    a = [1] * (n - 1)
    primes = []
    start = 2
    stop = math.floor(math.sqrt(n))

    while start <= n:
        if a[start - 2] == 1:
            primes.append(start)
            if start <= stop:
                i = start * 2
                while i <= n:
                    a[i - 2] = 0
                    i += start

        start += 1        

    return primes

def second(n):
    
    if n <= 1:
        return []

    size = n - 1
    is_prime = [True] * size
    primes = []

    for i in range(2, n + 1):
        if is_prime[i - 2]:
            primes.append(i)
            for j in range(i * i, n + 1, i):
                is_prime[j - 2] = False

    return primes

# only check odd numbers
def third(n):

    if n < 2:
        return []

    primes = [2]
    size = n // 2
    is_prime = [True] * size
    # print('is prime ', is_prime)
    for i in range(3, n + 1, 2):
        # print(i, is_prime[i // 2 - 1])
        if is_prime[i // 2 - 1]:
            primes.append(i)
            for j in range(i * i, n + 1, i * 2):
                # print('j=', j)
                is_prime[j // 2 - 1] = False
    
    return primes

# Given n, return all primes up to and including n.
def generate_primes(n):
    # return first(n)
    # return second(n)
    return third(n)

    # took almost 1 hour
    # return bf(n)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("prime_sieve.py", "prime_sieve.tsv",
                                       generate_primes))
