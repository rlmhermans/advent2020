import scala.io.Source

object Main extends App {
  val seq = readInput()
  println((for (line <- seq if checkPasswordValidity(line)) yield line).size)

  def readInput(): Seq[String] = {
    val bufferedSource = Source.fromFile("src/main/scala/input.txt")
    val lines =
      (for (line <- bufferedSource.getLines()) yield line).toSeq
    bufferedSource.close()
    lines
  }

  def checkPasswordValidity(password: String): Boolean = {
    val parts = password.split("[: -]")
    val charAtFirst =
      parts(4).charAt(parts(0).toInt - 1).toString().equals(parts(2))
    val charAtSecond =
      parts(4).charAt(parts(1).toInt - 1).toString().equals(parts(2))
    (charAtFirst && !charAtSecond) || (!charAtFirst && charAtSecond)
  }
}
