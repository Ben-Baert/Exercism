from math import sqrt

def _prime_candidate_generator(number):
    yield 2
    yield 3
    for n in range(6, int(sqrt(number)), 6):
        yield n + 1
        yield n - 1

def prime_factors(number):
    """
    Parameters
    ----------
    number : int

    Returns
    -------
    prime_factors : list

    Examples
    --------
    >>> prime_factors(1)
    []

    >>> prime_factors(20)
    [2, 2, 5]

    """
    factors = []
    prime_candidate_generator = _prime_candidate_generator(number)
    current_candidate = next(prime_candidate_generator)
    remainder = number #

    while True:
        while remainder % current_candidate == 0:
            factors.append(current_candidate)
            remainder //= current_candidate
        try:
            current_candidate = next(prime_candidate_generator)
        except StopIteration:
            if remainder > 1:
                factors.append(remainder)
            break

    return factors

if __name__ == '__main__':
    import doctest
    doctest.testmod()