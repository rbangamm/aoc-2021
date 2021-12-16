package algebra

import output._

case class Coordinate(x: Int, y: Int)

object Coordinate:
  given OutputFormat[Coordinate] with
    def toOutput(input: Coordinate): String = s"Answer (Coordinate): (${input.x}, ${input.y})"

  given Ordering[Coordinate] with
    def compare(x: Coordinate, y: Coordinate): Int = x.x.compare(y.x)
