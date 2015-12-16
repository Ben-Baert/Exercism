#from numpy import product

def slices(string_of_digits, slice_length):
    if slice_length > len(string_of_digits):
        raise ValueError("Your slices are larger than the length of your string.")
    return [[int(x) for x in string_of_digits[i:slice_length + i]]
            for i in range(len(string_of_digits) - slice_length + 1)]

def product(lst):
    x = 1
    for number in lst:
        x *= number
    return x

def largest_product(string_of_digits, slice_length):
    slices_list = slices(string_of_digits, slice_length)
    return max(product(slice_list) for slice_list in slices_list)