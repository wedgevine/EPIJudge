from test_framework import generic_test

def first(n):

    all = list(range(2, n + 1))
    primes = []

    while len(all) > 0:
        p = all[0]
        for i in all:
            



    return primes

# Given n, return all primes up to and including n.
def generate_primes(n):
    return first(n)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("prime_sieve.py", "prime_sieve.tsv",
                                       generate_primes))
