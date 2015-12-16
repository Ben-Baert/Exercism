def sieve(x):
    numbers_to_consider = range(2, x + 1)
    composite = []
    prime = []
    for number in numbers_to_consider:
        if number not in composite:
            prime.append(number)
            current = number
            while current <= x:
                current += number
                composite.append(current)
    return prime