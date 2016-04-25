class Anagram(word:String) {

    def matches(words:Seq[String]) : Seq[String] = {
        words.filter(isAnagram)
    }

    private val loweredWord = word.toLowerCase

    private def isAnagram(anagram:String) : Boolean = {
        val loweredAnagram = anagram.toLowerCase
        
        val isMatch = loweredWord.sorted == loweredAnagram.sorted
        val notIdentical = loweredWord != loweredAnagram

        isMatch && notIdentical
    }
}