import input.DataInput.given
import input._
import output._
import algebra._

object Day1:
  def compute(name: String, windowSize: Int): Int = compute2(name.resource, windowSize)

  def compute2(input: Seq[Int], windowSize: Int) : Int = 
    input
      .sliding(windowSize)
      .sliding(2)
      .count(value => value.head.head < value.last.last)
  object Math {
    def doSomething[A](number: A)(using numeric: Numeric[A]): A = {
      numeric.times(numeric.plus(number, number), number)
    }
  }


  def computeAndOutput(windowSize : Int): Unit = {
    val result = compute("day1", windowSize)

    Seq(Coordinate(0, 0), Coordinate(1, 1)).sorted
    Outputter.output(Math.doSomething(5))
    Outputter.output(Math.doSomething(10L))
    Outputter.output(Math.doSomething(3.0))

    Outputter.output(result)
    Outputter.output(result.toLong)
    Outputter.output('B')
    Outputter.output(Coordinate(4, 5))
  }

  case class Request(body: String, requestType: String = "GET")

  def response(): String = {
    val request = Request("{json: 'Good'}", requestType = "POST")

    func1(using request)
  }

  def func1(using request: Request): String = {
    func2
  }

  def func2(using request: Request): String = {
    request.body
  }
