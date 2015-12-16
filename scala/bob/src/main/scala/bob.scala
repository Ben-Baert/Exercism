class Bob {
    def hey(statement:String) : String = {
        if (statement.exists(_.isLetter) && statement.toUpperCase == statement) "Whoa, chill out!"
        else if (statement.endsWith("?")) "Sure."
        else if (statement.trim.isEmpty) "Fine. Be that way!"
        else "Whatever."
    }
}