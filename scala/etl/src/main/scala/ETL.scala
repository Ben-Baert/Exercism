object ETL {
  def transform(old: Map[Int, Seq[String]]): Map[String, Int] = {
    for {
      (score, words) <- old 
        word <- words
      }
      yield word.toLowerCase -> score
  }
}


