import scala.util.Random

class Robot {
    private var _name : String = newName

    def name : String = {
        _name
    }

    def reset() : Unit = {
        _name = newName
    }

    private def newName : String = {
        firstPartName + lastPartName
    }

    private def firstPartName : String = {
        Random.shuffle('A'.to('Z').toList).take(2).mkString
    }

    private def lastPartName : String = {
        Random.shuffle(100.to(999).toList).head.toString
    }

}