import scala.io.Source
import scala.collection.mutable.ListBuffer

object Main extends App {
  val bags = Source.fromFile("input").getLines().toList
  val bagsWithoutContent = bags.filter(!_.contains("no other bags"))
  val consistentlyNamedBags = bagsWithoutContent.map(_.replace("bags", "bag"))
  val upwards =
    consistentlyNamedBags.foldLeft(List[(String, String)]())((l, s) =>
      l ++ contentToBag(s)
    )
  val upwardsMap = upwards.groupBy(_._1).map { case (k, v) => (k, v.map(_._2)) }

  println(containingBags("shiny gold bag", Set[String]()).size)

  def contentToBag(s: String): ListBuffer[(String, String)] = {
    val parts = s.split(" contain ")
    val containedBags = parts(1).replace(".", "").split(", ")
    containedBags.foldLeft(ListBuffer[(String, String)]())((x, y) =>
      x += ((y.substring(2), parts(0)))
    )
  }

  def containingBags(color: String, uniqueBags: Set[String]): Set[String] = color match {
    case c if upwardsMap.contains(c) => upwardsMap(c).foldLeft(uniqueBags)((x, y) => x + y ++ containingBags(y, uniqueBags)) 
    case _ => Set[String]()
  }
}
