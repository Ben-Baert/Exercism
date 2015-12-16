class Hamming(dna1:String, dna2:String) {
    require(dna1.length == dna2.length)
    def distance =
        dna1.zip(dna2).count {
            case (a, b) => a != b
        }
}


object Hamming {
    def compute(dna1: String, dna2: String) : Int =
        new Hamming(dna1, dna2).distance
}