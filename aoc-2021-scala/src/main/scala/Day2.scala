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

  def computePartTwo : Int = {
    var aim = 0
    val res = DataInput.fromResource("day2").map(value => {
      val direction = value.split(" ")(0)
      val num = value.split(" ")(1).toInt
      if (direction == "forward") then (num, 0)
      else if (direction == "up") then (0, -num)
      else (0, num)
    }).foldLeft(0, 0){ case ((x, y), (a, b)) => {
      if (b == 0) then (x + a, y + aim * a)
      else { 
        aim += b
        (x + a, y)
      }
    } }
    res._1 * res._2
  }
}
