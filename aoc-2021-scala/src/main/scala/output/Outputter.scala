package output

object Outputter:
  def output[A](input: A)(using formatter: OutputFormat[A]): Unit =
    println(formatter.toOutput(input))