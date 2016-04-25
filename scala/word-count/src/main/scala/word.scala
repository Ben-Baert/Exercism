import scala.collection.mutable

class Phrase (phrase:String) {
    lazy val wordCount = {
        val counts = mutable.Map[String, Int]().withDefaultValue(0)
        
        phrase
            .toLowerCase
            .split("[ ,!:,.]+")
            .filter(_.matches("[\\d\\w\\']+"))
            .map(counts(_) += 1)

        counts
    }    
}
