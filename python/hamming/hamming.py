def distance(str1, str2):
    difference = 0
    for a, b in zip(str1, str2):
        if a != b:
            difference += 1
    return difference