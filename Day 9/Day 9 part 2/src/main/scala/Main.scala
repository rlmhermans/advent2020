import scala.io.Source

object Main extends App {
  val xmasData = Source.fromFile("input").getLines().map(_.toLong).toVector
  val preambuleSize = 25
  val validity = (preambuleSize to xmasData.size - 1).map(validNumber)
  val firstInvalidIndex = validity.indexOf(false) + preambuleSize
  val firstInvalidNumber = xmasData(firstInvalidIndex)

  println("Invalid number: " + firstInvalidNumber + " at index " + firstInvalidIndex)
  countDown(firstInvalidIndex-1)

  def validNumber(index: Int): Boolean = {
    val preambule = xmasData.slice(index - preambuleSize, index)
    val number = xmasData(index)
    val remainders = preambule.map(number - _)
    remainders.map(x => preambule.contains(x)).foldLeft(false)(_ || _)
  }

  def countDown(index: Int): Unit = {
    val found = contiguousSum(index, xmasData(index))

    found match {
      case Some(value) => {
        val contiguous = xmasData.slice(value, index + 1)
        val lowestValue = contiguous.min 
        val highestValue = contiguous.max 
        println("Found! Lowest value: " + lowestValue + " Highest value: " + highestValue)
        println("Part 2 answer: " + (lowestValue + highestValue) )
      }
      case None => countDown(index - 1)
    }
  }

  def contiguousSum(index: Int, acc: Long): Option[Int] = {
    acc match {
      case a if a < firstInvalidNumber => contiguousSum(index - 1, acc + xmasData(index - 1))
      case a if a == firstInvalidNumber => Some(index)  
      case _ => None
  }
}
}
