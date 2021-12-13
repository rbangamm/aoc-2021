import org.scalatest._
import matchers.should.Matchers._
import org.scalatest.funsuite.AnyFunSuite

class Day1Test extends AnyFunSuite:
  test("can compute day 1 part 1 output") {
    Day1.compute(1) shouldBe 1709
  }

  test("can compute day 1 part 2 output") {
    Day1.compute(3) shouldBe 1761
  }