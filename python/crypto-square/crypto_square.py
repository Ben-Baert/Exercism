import re
from math import sqrt, ceil

def encode(input_string):
    cleaned = re.sub(r"[^a-z1-9]", "", input_string.lower())
    nr_of_columns = ceil(sqrt(len(cleaned)))
    return " ".join("".join(cleaned[x] for x in range(i, len(cleaned), nr_of_columns)) for i in range(nr_of_columns))