import re

class Phone:
    def __init__(self, number):
        self._number = number

    @property
    def number(self):
        temp = re.sub(r"[^0-9]", "", self._number)
        if len(temp) != 10:
            if not (len(temp) == 11 and temp[0] == "1"):
                return "0000000000"
            return temp[1:]
        return temp

    def area_code(self):
        return self.number[:3]

    def pretty(self):
        return re.sub(r"([0-9]{3})([0-9]{3})([0-9]{4})", r"(\1) \2-\3", self.number)