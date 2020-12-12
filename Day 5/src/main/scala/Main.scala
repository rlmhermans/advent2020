import scala.io.Source

object Main extends App {
  type Range = (Int, Int)

  val seats = Source.fromFile("input.txt").getLines().toList
  val seatIDs = seats.map(x => seatRow(x, (0, 127)))
  println((seatIDs.min to seatIDs.max).diff(seatIDs))

  def seatRow(seat: String, range: Range): Int = seat match {
    case a if a.head == 'F' => seatRow(seat.tail, lower(range))
    case b if b.head == 'B' => seatRow(seat.tail, upper(range))
    case _                  => seatID(seat, range._1, (0, 7))
  }

  def seatID(seat: String, row: Int, range: Range): Int = seat match {
    case ""                 => row * 8 + range._1
    case a if a.head == 'L' => seatID(seat.tail, row, lower(range))
    case b if b.head == 'R' => seatID(seat.tail, row, upper(range))
  }

  def lower(whole: Range): Range = (whole._1, (whole._1 + whole._2) / 2)
  def upper(whole: Range): Range = ((whole._1 + whole._2) / 2 + 1, whole._2)
}
