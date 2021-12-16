package day16
import input.DataInput
import scala.annotation.tailrec

object Day16:

  sealed trait Packet:
    def version: Int
    def typeId: Int
  
  case class Literal(override val version: Int, override val typeId: Int, value: Int) extends Packet
  case class Operator(override val version: Int, override val typeId: Int, symbol: Int, packets: Seq[Packet] = Seq.empty) extends Packet

  // case class PacketSet(processing: Packet, processed: Seq[Packet]) {
  //   def processChunk(chunk: String): PacketSet = {
  //     // Check if chunk is complete
  //     // If it is move to processed, excesss stays in Processing
  //   }
  // }

  case class ProcessingLiteral(current: String):
    lazy val isDone: Boolean = leadingChar.map(_ == '0').getOrElse(false)
    lazy val leadingChar: Option[Char] = current.lift(lastLeadingIndex)
    def lastLeadingIndex: Int = Math.floor(current.length / 5D).toInt * 5
    def + (chunk: String): ProcessingLiteral = copy(current = current + chunk)

    def asDecimal: Int = current.dropRight(current.length % 5).sliding(5).foldLeft("") { 
      case (binaryString, chunk) => binaryString + chunk.tail
    }.binaryToDecimal

  @tailrec
  final def computeLiteral(data: String, result: String = ""): Int = 
    data.head match {
      case '1' => computeLiteral(data.drop(5), result + data.slice(1, 5))
      case '0' => (result + data.slice(1, 5)).binaryToDecimal
    }

  def compute(input: String) : Seq[Int] = {
    // val input = DataInput.fromResource("day16").head
    // val set = PacketSet(processing = "", processed = Seq.empty)

    // input.toStream.foldLeft(set) { case(instructions, nextCharacter) =>
    //   set.processChunk(nextCharacter.toString.toBinary)
    // }

    var processing: String = ""
    var version: Option[Int] = None
    var typeId: Option[Int] = None
    var literal: ProcessingLiteral = ProcessingLiteral("")
    var result: Seq[Int] = Seq.empty
    // var data: Option[String] = None

    input.foreach { nextCharacter =>
      processing += nextCharacter.toString.hexToBinary.reverse.padTo(4, '0').reverse
      
      (version, typeId) match {
        case (None, None) => {
          version = Some(processing.take(3).binaryToDecimal)
          processing = processing.drop(3)
        }
        case (Some(_), None) => {
          typeId = Some(processing.take(3).binaryToDecimal)
          processing = processing.drop(3)
        }
        case (Some(_), Some(4)) => {
          literal = literal + processing
          processing = ""
        }
        case (Some(_), Some(value)) => throw java.lang.IllegalArgumentException(s"No idea wtf $value is")
      }

      println("Current Literal: " + literal.current)
      println("Current Last Index: " + literal.lastLeadingIndex)
      println("-------------")

      if (literal.isDone) {
        result = result :+ literal.asDecimal
        literal = ProcessingLiteral("")
        println("DONE ONE LITERAL" + result)
      }

    }

    result
    // val binaryString = input.hexToBinary
    // val version = binaryString.take(3).binaryToDecimal
    // val typeId = binaryString.slice(3, 6).binaryToDecimal
    // typeId match {
    //   case 4 => Seq(computeLiteral(binaryString.drop(6)))
    //   case _ => Seq(-1)
    // }
  }