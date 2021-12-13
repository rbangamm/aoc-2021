import org.scalatest._
import matchers.should.Matchers._
import org.scalatest.funsuite.AnyFunSuite

class Day2Test extends AnyFunSuite:
  test("can compute day 2 part 1 output") {
    Day2.computePartOne shouldBe 1427868
  }
  test("can compute day 2 part 2 output") {
    Day2.computePartTwo shouldBe 1568138742
  }