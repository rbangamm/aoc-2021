object Day2 {
  def computePartOne : Int = {
    val res = DataInput.fromResource("day2").map(value => {
      val direction = value.split(" ")(0)
      val num = value.split(" ")(1).toInt
      if (direction == "forward") then (num, 0)
      else if (direction == "up") then (0, -num)
      else (0, num)
    }).foldLeft(0, 0){ case ((x, y), (a, b)) => (x + a, y + b) }
    res._1 * res._2
  }

  case class Position(aim: Int = 0, depth: Int = 0, horizontal: Int = 0):
    def up(value: Int): Position = copy(aim = aim - value)
    def down(value: Int): Position = copy(aim = aim + value)
    def forward(value: Int): Position = copy(
      horizontal = horizontal + value, 
      depth = depth + aim * value
    )
    lazy val calculate : Int = horizontal * depth

  def computePartTwo : Int = {
    DataInput.fromResource("day2")
      .map(_.split(" "))
      .foldLeft(Position()) { case(position, command) =>
        command match {
          case Array("down", value) => position.down(value.toInt)
          case Array("up", value) => position.up(value.toInt)
          case Array("forward", value) => position.forward(value.toInt)
        }
      }.calculate

    // var aim = 0L
    // val res = DataInput.fromResource("day2").map(value => {
    //   val direction = value.split(" ")(0)
    //   val num = value.split(" ")(1).toInt
    //   if (direction == "forward") then (num, 0)
    //   else if (direction == "up") then (0, -num)
    //   else (0, num)
    // }).foldLeft(0, 0){ case ((x, y), (a, b)) => {
    //   if (b == 0) then (x + a, y + aim * a)
    //   else { 
    //     aim += b
    //     (x + a, y)
    //   }
    // } }
    // res._1 * res._2
  }
}
