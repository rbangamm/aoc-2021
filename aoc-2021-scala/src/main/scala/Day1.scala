object Day1:
  def compute(windowSize : Int) : Int = 
    DataInput.fromResource("day1")
      .map(_.toInt)
      .sliding(windowSize)
      .sliding(2)
      .count(value => value.head.head < value.last.last)

