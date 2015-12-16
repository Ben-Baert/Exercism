from itertools import count
from math import sqrt

def prime_candidates():
    yield 2
    yield 3
    for n in count(6, 6):
        yield n - 1
        yield n + 1

def nth_prime(n):
    primes = []
    candidates = prime_candidates()

    while len(primes) < n:
        candidate = next(candidates)
        for prime in primes:
            if prime > sqrt(candidate):
                primes.append(candidate)
                break
            if candidate % prime == 0:
                break
        else:
            primes.append(candidate)

    return primes[-1]