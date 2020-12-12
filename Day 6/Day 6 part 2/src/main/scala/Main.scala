import scala.io.Source
import scala.collection.mutable.ListBuffer

object Main extends App {
  val bags = Source.fromFile("input").getLines().toList
  val bagsWithoutContent = bags.filterNot(_.contains("no other bags"))
  val consistentlyNamedBags = bagsWithoutContent.map(_.replace("bags", "bag"))
  val contents =
    consistentlyNamedBags.foldLeft(List[(String, String)]())((l, s) =>
      l ++ bagToContent(s)
    )

  val contentsMap =
    contents.groupBy(_._1).map({ case (k, v) => (k, v.map(_._2)) })
    
  println(containingBags("shiny gold bag"))

  def bagToContent(s: String): ListBuffer[(String, String)] = {
    val parts = s.split(" contain ")
    val containedBags = parts(1).replace(".", "").split(", ")
    containedBags.foldLeft(ListBuffer[(String, String)]())((x, y) =>
      x += ((parts(0), y))
    )
  }

  def containingBags(color: String): Int =
    color match {
      case c if contentsMap.contains(c) => {
        contentsMap(c)
          .map(x => {
            val num = x.charAt(0).asDigit;
            num + num * containingBags(x.substring(2))
          }).sum
      }
      case _ => 0
    }
}
