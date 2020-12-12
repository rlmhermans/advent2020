import scala.io.Source

object Main extends App {
  val jolts = Source.fromFile("input").getLines().map(_.toInt).toVector.sorted
  val withOutput = 0 +: jolts
  val adapters = withOutput :+ withOutput.last + 3
  val allDistances = adapters.sliding(2).map(x => x(1) - x(0)).toVector
  val ones = allDistances.count(_ == 1)
  val threes = allDistances.count(_ == 3)
  println("Part 1: " + ones * threes)
  println("Part 2: " + nrOfCombos(allDistances))

  def nrOfCombos(distances: Vector[Int]): Long = distances match {
    case Vector() => 1
    case _ => {
      val restAndSize = group(distances)
      restAndSize._2 * nrOfCombos(restAndSize._1)
    }
  }

  def group(distances: Vector[Int]): (Vector[Int], Int) = {
    val group = distances.slice(0, distances.indexOf(3))
    val rest = distances.slice(distances.indexOf(3) + 1, distances.size)
    (rest, multiplication(group.size))
  }

  def multiplication(groupSize: Int): Int = groupSize match {
    case 2 => 2
    case 3 => 4
    case 4 => 7
    case _ => 1
  }
}
