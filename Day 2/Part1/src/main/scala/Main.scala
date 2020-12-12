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
    val parts = password.split(": ")
    val policy = parts(0).split(" ")
    val range = policy(0).split("-")
    val occurences = parts(1).map(_.toString()).count(x => x == policy(1))
    occurences >= range(0).toInt && occurences <= range(1).toInt
  }
}