class Anagram(word:String) {
    val loweredWord = word.toLowerCase

    def matches(words:Seq[String]) : Seq[String] = {
        words.filter(x => isAnagram(x))
    }

    private def isAnagram(anagram:String) : Boolean = isMatch(anagram) && notIdentical(anagram)

    private def isMatch(anagram:String) : Boolean = loweredWord.sorted == anagram.toLowerCase.sorted

    private def notIdentical(anagram:String) : Boolean = loweredWord != anagram.toLowerCase

}