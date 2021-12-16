package output

trait OutputFormat[A]:
  def toOutput(input: A): String

object OutputFormat:
  given OutputFormat[Int] with
    def toOutput(input: Int): String = s"Answer: $input"

  given OutputFormat[Long] with
    def toOutput(input: Long): String = s"Answer (Long): $input"

  given OutputFormat[Char] with
    def toOutput(input: Char): String = s"Answer (Char): ${input.toString}"

  given OutputFormat[Double] with
    def toOutput(input: Double): String = s"Answer (Double): ${input.toString}"