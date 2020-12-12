import scala.io.Source

object Main extends App {
  type Execution = (Array[String], Int, Int)
  val initProgram = Source.fromFile("input").getLines().toArray

  var current = 0;

  while(true) {
    val original = initProgram(current)

    original match {
      case i if i.contains("nop") =>
        initProgram(current) = i.replace("nop", "jmp")
      case i if i.contains("jmp") =>
        initProgram(current) = i.replace("jmp", "nop")
      case _ => 
    }
    run((initProgram, 0, 0))
    initProgram(current) = original
    current += 1;
  }

  def run(exec: Execution): Execution = {
    val program = exec._1.clone()
    val current = exec._2
    val acc = exec._3
    if(current == initProgram.size) println(acc)
    val instruction = program(current)
    program(current) = ""

    instruction match {
      case "" => exec
      case i if i.contains("acc") =>
        run(program, current + 1, acc + instruction.split(" ")(1).toInt)
      case i if i.contains("jmp") =>
        run(program, current + instruction.split(" ")(1).toInt, acc)
      case i if i.contains("nop") => run(program, current + 1, acc)
    }
  }

}
