import scala.math.pow

object Day3 {

  def toDec(seq : Seq[Int]) : Int = {
    seq
      .reverse
      .zipWithIndex
      .foldLeft(0, 0){case ((x, y), (a, b)) => (x + scala.math.pow(2, b).intValue * a, 0)}._1
  }

  def mostCommon(seq: Seq[String]) : Seq[Int] = {
    val res = seq.map(_.toCharArray.map(_.toInt - 48))
      .transpose
      .map(_.groupBy(identity).mapValues(_.size))
    res.map(value => value.filter(_._2 == value.maxBy(_._2)._2))
      .map(value => {
        if (value.size == 1) then value.keys.head
        else 1
      })
  }

  def computePartOne : Int = {
    val res = DataInput.fromResource("day3")
      .map(_.toCharArray.map(_.toInt - 48))
      .transpose
      .map(_.groupBy(identity).mapValues(_.size).maxBy(_._2)._1)
    toDec(res) * toDec(res.map(1-_))
  }

  def computePartTwo : Int = {
    val input = DataInput.fromResource("day3")
    def computeO2(in : Seq[String], i : Int) : Int = {
      if (in.length == 1) then toDec(in(0).toCharArray.map(_.toInt - 48))
      else computeO2(in.filter(x => x(i).toInt - 48 == mostCommon(in)(i)), i+1)
    }
    def computeCO2(in : Seq[String], i : Int) : Int = {
      if (in.length == 1) then toDec(in(0).toCharArray.map(_.toInt - 48))
      else computeCO2(in.filter(x => x(i).toInt - 48 == mostCommon(in).map(1-_)(i)), i+1)
    }
    computeO2(input, 0) * computeCO2(input, 0)
  }
}
