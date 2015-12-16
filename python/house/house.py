VERSES = [
('horse and the hound and the horn', 'belonged to'),
('farmer sowing his corn', 'kept'),
('rooster that crowed in the morn', 'woke'),
('priest all shaven and shorn', 'married'),
('man all tattered and torn', 'kissed'),
('maiden all forlorn', 'milked'),
('cow with the crumpled horn', 'tossed'),
('dog', 'worried'),
('cat', 'killed'),
('rat', 'ate'),
('malt', 'lay in'),
('house', 'Jack built')]


def verse(nr):
    return "This is" + ''.join(" the " + verse[0] +
        (" " if index == nr else "\n") + "that " + verse[1]
        for index, verse in enumerate(VERSES[-nr-1:]))


def rhyme():
    return ".\n\n".join(verse(i) for i in range(12)) + "."