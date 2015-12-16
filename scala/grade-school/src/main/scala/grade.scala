import scala.collection.immutable.SortedMap

class School {
    var db = Map.empty[Int,Seq[String]].withDefaultValue(Seq())

    def add(student:String, gradeNr:Int) = {
        db = db.updated(gradeNr, grade(gradeNr) :+ student)
    }

    def grade(gradeNr: Int): Seq[String] = {
        db.getOrElse(gradeNr, Vector.empty)
    }

    def sorted = {
        SortedMap(db.toSeq:_*).mapValues(_.sorted)
    }
}