class Matrix:
    def __init__(self, input_string):
        self.rows = [[int(y) for y in x.split(" ")] for x in input_string.split("\n")]

    @property
    def columns(self):
        return [list(column) for column in zip(*self.rows)]