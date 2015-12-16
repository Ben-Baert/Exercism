from string import hexdigits

def hexa(hex_string):
    return sum(hexdigits.index(current_digit) * 16**current_position for current_position, current_digit in enumerate(hex_string.lower()[::-1]))