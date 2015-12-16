def is_palindrome(i, j):
    return str(i * j) == str(i * j)[::-1]

def generate_palindrome(max_factor, min_factor=0):
    for i in range(min_factor, max_factor + 1):
        for j in range(i, max_factor + 1):
            if is_palindrome(i, j):
                yield i * j, (i, j)

def smallest_palindrome(max_factor, min_factor=0):
    for palindrome in generate_palindrome(max_factor, min_factor):
        return palindrome

def largest_palindrome(max_factor, min_factor=0):
    max_palindrome = (0,)
    for palindrome in generate_palindrome(max_factor, min_factor):
        if palindrome[0] > max_palindrome[0]:
            max_palindrome = palindrome
    return max_palindrome