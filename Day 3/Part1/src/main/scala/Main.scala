import scala.io.Source

object Main extends App {
  println(multiplyTreeCount)

  def multiplyTreeCount(): BigInt = {
    var product = BigInt(1)
    product *= countTrees(1, 1)
    product *= countTrees(3, 1)
    product *= countTrees(5, 1)
    product *= countTrees(7, 1)
    product *= countTrees(1, 2)
    product
  }

  def countTrees(stepX: Int, stepY: Int): Int = {
    var trees = 0
    var x = 0
    var y = 0
    val lines = readInput()

    while (y < lines.size - 1) {
      y += stepY
      x += stepX
      if (x >= lines(y).size) {
        x -= lines(y).size
      }

      if (lines(y).charAt(x) == '#') {
        trees += 1
      }
    }

    trees
  }

  def readInput(): Seq[String] = {
    val bufferedSource = Source.fromFile("src/main/scala/input.txt")
    val lines =
      (for (line <- bufferedSource.getLines()) yield line).toSeq
    bufferedSource.close()
    lines
  }
}
