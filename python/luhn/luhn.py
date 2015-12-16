class Luhn:
    def __init__(self, number):
        self.number = number

    def _number_to_list_of_digits(self):
        digits_list = []
        remainder = self.number
        while remainder > 0:
            digit = remainder % 10
            digits_list.append(digit)
            remainder //= 10
        return digits_list

    def _transform_list_of_digits(self):
        list_of_digits = self._number_to_list_of_digits()
        return [(digit*2 if digit <= 4 else digit*2 - 9)
                if index % 2 == 0 else digit
                for index, digit in enumerate(list_of_digits, start=1)]

    def addends(self):
        transformed_list_of_digits = self._transform_list_of_digits()
        return transformed_list_of_digits

    def checksum(self):
        return sum(self.addends()) % 10

    @staticmethod
    def create(number):
        check_digit = (10 - Luhn(number * 10).checksum()) % 10
        return 10 * number + check_digit

    def is_valid(self):
        return self.checksum() == 0