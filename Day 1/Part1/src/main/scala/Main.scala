import scala.io.Source
import scala.collection.Searching.Found

object Main extends App {
  val seq = readInput()
  val pair = findPair(2020, seq)
  println(pair._1 * pair._2)

  def readInput(): Seq[Int] = {
    val bufferedSource = Source.fromFile("src/main/scala/input.txt")
    val lines =
      for (line <- bufferedSource.getLines()) yield line
    bufferedSource.close()
    lines
  }

  def findPair(reqSum: Int, expenses: Seq[Int]): (Int, Int) = {
    val sortedSeq = seq.sorted.slice(0, seq.length / 2 + 1)
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
}
