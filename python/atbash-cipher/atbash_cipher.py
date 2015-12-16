import re
from string import ascii_lowercase

TRANTAB = str.maketrans(ascii_lowercase, ascii_lowercase[::-1])

def encode(string):
    string = re.sub(r"[^a-z0-9]", '', string.lower())
    string = ' '.join(string[i:i+5] for i in range(0, len(string), 5))
    return string.translate(TRANTAB)

def decode(string):
    string = string.replace(" ", "")
    return string.translate(TRANTAB)