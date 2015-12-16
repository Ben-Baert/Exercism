def verse(verse_nr):
    if verse_nr == 0:
        return "No more bottles of beer on the wall, no more bottles of beer.\nGo to the store and buy some more, 99 bottles of beer on the wall.\n"
    if verse_nr == 1:
         return "1 bottle of beer on the wall, 1 bottle of beer.\nTake it down and pass it around, no more bottles of beer on the wall.\n"
    if verse_nr == 2:
        return "2 bottles of beer on the wall, 2 bottles of beer.\nTake one down and pass it around, 1 bottle of beer on the wall.\n"
    return "{0} bottles of beer on the wall, {0} bottles of beer.\nTake one down and pass it around, {1} bottles of beer on the wall.\n".format(verse_nr, verse_nr - 1)

def song(start, finish=0):
    return "\n".join(verse(verse_index) for verse_index in range(start, finish - 1, -1)) + "\n"