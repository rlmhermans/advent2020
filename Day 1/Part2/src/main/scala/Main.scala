import scala.io.Source
import scala.collection.Searching.Found

object Main extends App {
  val triplet = findTriplet(2020, readInput())
  println(triplet._1 * triplet._2 * triplet._3)

  def readInput(): Seq[Int] = {
    val bufferedSource = Source.fromFile("src/main/scala/input.txt")
    val lines =
      (for (line <- bufferedSource.getLines()) yield line.toInt).toIndexedSeq
    bufferedSource.close()
    lines
  }

  def findPair(reqSum: Int, expenses: Seq[Int]): (Int, Int) = {
    val sortedSeq = expenses.sorted.slice(0, expenses.length / 2 + 1)
    var foundPair = (-1, -1)
    sortedSeq.foreach(x => {
      val reqNum = reqSum - x
      val result = sortedSeq.search(reqNum)
      if (result.isInstanceOf[Found]) {
        foundPair = (x, reqNum)
      }
    })
    foundPair
  }

  def findTriplet(reqSum: Int, expenses: Seq[Int]): (Int, Int, Int) = {
    var foundTriplet = (-1, -1, -1)
    expenses.foreach(x => {
      val reqNum = reqSum - x
      val listWithoutX = expenses.diff(Seq(x))
      val pair = findPair(reqNum, listWithoutX)
      if (pair != (-1, -1)) {
        foundTriplet = (pair._1, pair._2, x)
      }
    })
    foundTriplet
  }
}