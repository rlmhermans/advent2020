import scala.io.Source

object Main extends App {
  //85848519
  //To find the encryption weakness, add together the smallest and largest number in this contiguous range; in this example, these are 15 and 47, producing 62.
  val xmasData = Source.fromFile("input").getLines().map(_.toLong).toVector
  val preambuleSize = 25
  val validity = (preambuleSize to xmasData.size - 1).map(validNumber)
  println(xmasData(validity.indexOf(false) + preambuleSize))

  def validNumber(index: Int): Boolean = {
    val preambule = xmasData.slice(index - preambuleSize, index)
    val number = xmasData(index)
    val remainders = preambule.map(number - _)
    remainders.map(x => preambule.contains(x)).foldLeft(false)(_ || _)
  }
}
