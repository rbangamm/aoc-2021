import javax.xml.crypto.Data
object Day4 {
  def computePartOne : Int = {
    val input = DataInput.fromResource("day4").map(_.strip).filter(_ != "")
    val numbers = input(0).split(",").map(_.toInt)
    val boards = input.slice(1, input.length).grouped(5).map(_.map(_.strip.split(" ").map(_.toInt)))
    def markBoards(numbers : Seq[Int], boards : Seq[Seq[Seq[Int]]], i : Int) : Int = {
      val res = boards.map(_.map(_.map(value => if numbers(i) == value then -value else value)))
      0
    }
    0
  }

  def computePartTwo : Int = {
    0
  }
}
