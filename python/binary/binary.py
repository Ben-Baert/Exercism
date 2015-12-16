def parse_binary(binary_string):
    """Standard implementation"""
    return int(binary_string, 2)

def parse_binary(binary_string):
    """Own implementation"""
    if any(digit not in '01' for digit in binary_string):
        raise ValueError("Input must be binary")
    return sum(2**current for current, value in enumerate(binary_string[::-1]) if value == '1')