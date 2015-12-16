def slices(string_of_digits, slice_length):
    if not 1 <= slice_length <= len(string_of_digits):
        raise ValueError("Your slices are larger than the length of your string.")
    return [[int(x) for x in string_of_digits[i:slice_length + i]]
            for i in range(len(string_of_digits) - slice_length + 1)]