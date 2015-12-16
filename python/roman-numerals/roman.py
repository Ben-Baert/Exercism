from collections import OrderedDict

def numeral(number_to_convert):
    numerals = OrderedDict()
    numerals[1000] = "M"
    numerals[900] = "CM"
    numerals[500] = "D"
    numerals[400] = "CD"
    numerals[100] = "C"
    numerals[90] = "XC"
    numerals[50] = "L"
    numerals[40] = "XL"
    numerals[10] = "X"
    numerals[9] = "IX"
    numerals[5] = "V"
    numerals[4] = "IV"
    numerals[1] = "I"

    roman = ""
    remainder = number_to_convert

    for arabic in numerals:
        times, remainder = divmod(remainder, arabic)
        roman += numerals[arabic] * times
        if not remainder:
            break
    return roman