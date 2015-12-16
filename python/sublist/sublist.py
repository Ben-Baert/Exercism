SUBLIST = 1
SUPERLIST = 2
EQUAL = 3
UNEQUAL = 4

def is_sublist(lst1, lst2):
    if not lst1 or any(lst1 == lst2[i:i+len(lst1)] for i in range(len(lst2))):
        return True
    return False

def is_superlist(lst1, lst2):
    return is_sublist(lst2, lst1)

def check_lists(lst1, lst2):
    if lst1 == lst2:
        return EQUAL
    if len(lst1) <= len(lst2) and is_sublist(lst1, lst2):
        return SUBLIST
    if len(lst1) > len(lst2) and is_superlist(lst1, lst2):
        return SUPERLIST
    return UNEQUAL