class Phrase(sentence:String) {
    def wordCountIdiomatic = {
        sentence.toLowerCase.split("[ :!.,]+").filter(_.matches("[0-9a-z']+")).groupBy(identity).mapValues(_.size)
    }
    def wordCountEfficient = {
        val counts = collection.mutable.Map[String, Int]().withDefaultValue(0)
        for (rawWord <- sentence.toLowerCase.split("[ ,!:,.]+").filter(_.matches("[0-9a-z']+"))) {
            counts(rawWord) += 1
        }
        counts
    }
    def wordCount = wordCountEfficient
}