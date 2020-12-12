import scala.io.Source

object Main extends App {
  val creds = Source
    .fromFile("src/main/scala/input.txt")
    .getLines()
    .mkString(";")
    .split(";;")
    .toList
  val mandatory = List("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid")
  val hairColors = List("amb", "blu", "brn", "gry", "grn", "hzl", "oth")
  println(check(creds))

  def check(creds: List[String]): Int = creds match {
    case Nil => 0
    case x :: xs =>
      (if (fieldsPresent(x) && fieldsValid(x.split("[ ;]").toList)) 1
       else 0) + check(xs)
  }

  def fieldsPresent(cred: String): Boolean = mandatory.forall(cred.contains(_))

  def fieldsValid(cred: List[String]): Boolean = cred match {
    case Nil     => true
    case x :: xs => validField(x) && fieldsValid(xs)
  }

  def validField(field: String): Boolean = field match {
    case f if f.startsWith("byr") => inRange(1920, 2002, f)
    case f if f.startsWith("iyr") => inRange(2010, 2020, f)
    case f if f.startsWith("eyr") => inRange(2020, 2030, f)
    case f if f.startsWith("hgt") => hgtValid(f.split(":")(1))
    case f if f.startsWith("hcl") => f.split(":")(1).matches("#[0-9a-f]{6}")
    case f if f.startsWith("ecl") => hairColors.contains(f.split(":")(1))
    case f if f.startsWith("pid") => f.split(":")(1).matches("[0-9]{9}")
    case _                        => true
  }

  def inRange(x: Int, y: Int, f: String): Boolean =
    (x to y).contains(f.split(":")(1).toInt)

  def hgtValid(hgt: String): Boolean = hgt match {
    case h if h.contains("cm") => (150 to 193).contains(h.split("cm")(0).toInt)
    case h if h.contains("in") => (59 to 76).contains(h.split("in")(0).toInt)
    case _                     => false
  }
}
