class DNA(strand:String) {
    strand.foreach(checkNucleotide)

    def count(nucleotide:Char) : Int = {
        checkNucleotide(nucleotide:Char)
        strand.count(_ == nucleotide)
    }

    def nucleotideCounts : Map[Char,Int] = {
        Map(
            'A' -> count('A'),
            'T' -> count('T'),
            'C' -> count('C'),
            'G' -> count('G')
        )
    }

    private def checkNucleotide(nucleotide: Char) = if (!"ATCG".contains(nucleotide)) throw new IllegalArgumentException
}