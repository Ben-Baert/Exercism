INT_TO_RANK = ['',
'first',
'second',
'third',
'fourth',
'fifth',
'sixth',
'seventh',
'eighth',
'ninth',
'tenth',
'eleventh',
'twelfth']

GIFTS = [
'twelve Drummers Drumming',
'eleven Pipers Piping',
'ten Lords-a-Leaping',
'nine Ladies Dancing',
'eight Maids-a-Milking',
'seven Swans-a-Swimming',
'six Geese-a-Laying',
'five Gold Rings',
'four Calling Birds',
'three French Hens',
'two Turtle Doves',
'a Partridge in a Pear Tree']


def sing():
    return verses(1, 12)

def verse(nr):
    base = "On the {} day of Christmas my true love gave to me, ".format(INT_TO_RANK[nr])
    base += ', '.join(gift if current < nr - 1 or nr == 1 else 'and ' + gift for current, gift in enumerate(GIFTS[-nr:]) )
    base += '.\n'
    return base

def verses(min_nr, max_nr):
    return '\n'.join(verse(nr) for nr in range(min_nr, max_nr + 1)) + "\n"