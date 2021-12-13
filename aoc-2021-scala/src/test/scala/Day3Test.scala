import org.scalatest._
import matchers.should.Matchers._
import org.scalatest.funsuite.AnyFunSuite

class Day3Test extends AnyFunSuite:
  test("can compute day 3 part 1 output") {
    Day3.computePartOne shouldBe 2250414
  }
  test("can compute day 3 part 2 output") {
    Day3.computePartTwo shouldBe 6085575
  }