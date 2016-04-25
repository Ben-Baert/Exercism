class PhoneNumber(input:String) {

    private val validNumber = {
        val separators = "\\D*"
        val areaCode, localCode = "\\d{3}"
        val personalCode = "\\d{4}"
        s"^1?$separators($areaCode)$separators($localCode)$separators($personalCode)$$".r
    }
    

    val (areaCode, localCode, personalCode) : (String, String, String) = input match {
        case validNumber(areaCode, localCode, personalCode) => (areaCode, localCode, personalCode)
        case _                                        => ("0" * 3, "0" * 3, "0" * 4)
    }

    val number : String = areaCode + localCode + personalCode

    override def toString = s"($areaCode) $localCode-$personalCode"
}