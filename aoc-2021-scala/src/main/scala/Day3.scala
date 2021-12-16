import scala.math.pow
import scala.annotation.tailrec
import input.DataInput

object Day3 {

  def toDec(seq : Seq[Int]) : Int = {
    Integer.parseInt(seq.mkString, 2)
      // .zipWithIndex
      // .foldLeft(0, 0){case ((x, y), (a, b)) => (x + scala.math.pow(2, b).intValue * a, 0)}._1
  }

  def mostCommon(seq: Seq[String]) : Seq[Int] = {
    seq.map(_.toCharArray.map(_.asDigit))
      .transpose
      .map(_.groupMapReduce(identity)(_ => 1)(_ + _))
      .map(value => value.filter { case(_, count) => count == value.values.max } )
      .map(value => {
        if (value.size == 1) then value.keys.head
        else 1
      })
  }

  def computePartOne : Int = {
    val res = DataInput.fromResource("day3")
      .map(_.toCharArray.map(_.asDigit))
      .transpose
      .map(_.groupBy(identity).mapValues(_.size).maxBy(_._2)._1)
    toDec(res) * toDec(res.map(1-_))
  }

  def computePartTwo : Int = {
    val input = DataInput.fromResource("day3")

    @tailrec
    def computeO2(in : Seq[String], i : Int) : Int = {
      if (in.length == 1) then toDec(in(0).toCharArray.map(_.asDigit))
      else computeO2(in.filter(x => x(i).asDigit == mostCommon(in)(i)), i+1)
    }

    @tailrec
    def computeCO2(in : Seq[String], i : Int) : Int = {
      if (in.length == 1) then toDec(in(0).toCharArray.map(_.asDigit))
      else computeCO2(in.filter(x => x(i).asDigit == mostCommon(in).map(1-_)(i)), i+1)
    }
    computeO2(input, 0) * computeCO2(input, 0)
  }
}
