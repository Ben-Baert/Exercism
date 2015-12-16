class PhoneNumber(rawNumber:String) {

    def number : String = {
        cleanNumber match {
            case valid(num) => num
            case _ => "0" * 10
        }
    }

    def areaCode : String = {
        number.substring(0, 3)
    }

    def exchangeCode : String = {
        number.substring(3, 6)
    }

    def subscriberNumber : String = {
        number.substring(6, 10)
    }

    override def toString : String = {
        s"($areaCode) $exchangeCode-$subscriberNumber"
    }

    private val valid = """^1?(\d{10})$""".r

    private val cleanNumber = rawNumber.replaceAll("""[^\d]""", "")
}