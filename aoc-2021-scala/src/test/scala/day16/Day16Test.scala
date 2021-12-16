package day16
import org.scalatest._
import matchers.should.Matchers._
import org.scalatest.funsuite.AnyFunSuite

class Day16Test extends AnyFunSuite:

  test("Can convert a single literal") {
    Day16.compute("D2FE28") shouldBe Seq(2021)
  }

  test("Can convert multiple literlas") {
    Day16.compute("D2FE28D2FE28") shouldBe Seq(2021, 2021)
  }