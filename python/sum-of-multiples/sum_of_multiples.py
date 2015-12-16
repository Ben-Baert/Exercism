def sum_of_multiples(x, multiples=[3, 5]):
    return sum(number for number in range(1, x)
        if any(number % multiple == 0
            for multiple in multiples
            if multiple > 0))