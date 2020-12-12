import scala.io.Source

object Main extends App {
  val offSets = (-1 to 1)
  val layout = Source.fromFile("input").getLines().toVector
  val yMax = layout.size - 1
  val xMax = layout.head.size - 1
  val chairLocations =
    layout.zipWithIndex.flatMap({ case (e, i) => chairs(e, i) }).toSet
  println("Part 2: " + stableState(chairLocations))

  def chairs(line: String, y: Int): Set[(Int, Int)] = {
    (for (x <- line.zipWithIndex if (validChair(x._1))) yield (x._2, y)).toSet
  }

  def validChair(c: Char): Boolean = c match {
    case 'L' => true
    case _   => false
  }

  def stableState(state: Set[(Int, Int)]): Int = {
    val nextPhase = step(state)

    if(nextPhase.equals(state)) nextPhase.size else stableState(nextPhase)
  }

  def step(state: Set[(Int, Int)]): Set[(Int, Int)] = {
    val personsLeft = state.filter(checkDirections(_, state) < 5)
    personsLeft ++ chairLocations.filter(x => !state.contains(x) && checkDirections(x, state) == 0)
  }

  def checkDirections(person: (Int, Int), state: Set[(Int, Int)]): Int = {
    val directions = offSets.flatMap(x => offSets.map(y => (x, y))).filterNot(_ == (0,0))
    val emptyDirections = directions.map(directionEmpty(person, _, state))
    emptyDirections.count(_ == false)
  }

  def directionEmpty(cell: (Int, Int), direction: (Int, Int), state: Set[(Int, Int)]): Boolean = {
    val nextCell = (cell._1 + direction._1, cell._2 + direction._2)
    val chairOnNextCell = chairLocations.contains(nextCell)

    if(chairOnNextCell) !state.contains(nextCell) else 
    if(nextCell._1 == -1 || nextCell._2 == -1 || nextCell._1 == xMax +1 || nextCell._2 == yMax +1) true else directionEmpty(nextCell, direction, state)
  }
  
  def neighbours(person: (Int, Int), state: Set[(Int, Int)]): Int = {
    val neighbour = (for {
      x <- (person._1 - 1 to person._1 + 1) if x >= 0 && x <= xMax
      y <- (person._2 - 1 to person._2 + 1) if y >= 0 && y <= yMax
    } yield (x, y)).filter(_ != person).filter(state.contains)
    
    neighbour.size
  }
}
