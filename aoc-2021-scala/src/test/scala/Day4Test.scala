import org.scalatest._
import matchers.should.Matchers._
import org.scalatest.funsuite.AnyFunSuite

class Day4Test extends AnyFunSuite:
  test("can compute day 3 part 1 output") {
    Day4.computePartOne shouldBe 4512
  }
  test("can compute day 3 part 2 output") {
    Day4.computePartTwo shouldBe 10030
  }