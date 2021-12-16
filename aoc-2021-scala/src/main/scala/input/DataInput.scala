package input

import scala.io.Source
import scala.annotation.targetName
import java.io.File
import java.nio.file.{Files, Paths}
import scala.collection.JavaConverters._


sealed trait DataInput:
  def rawStrings: Seq[String]

case class Resource(name: String) extends DataInput:
  override def rawStrings: Seq[String] = Source.fromResource(name).getLines.toVector

case class File(fileName: String) extends DataInput:
  override def rawStrings: Seq[String] = Source.fromResource(fileName).getLines.toVector


object DataInput:
  def fromResource(name: String): Seq[String] = Source.fromResource(name).getLines.toVector

  given resourceNameToSeqInt: Conversion[DataInput, Seq[Int]] with
    def apply(input: DataInput): Seq[Int] = input.rawStrings.map(_.toInt)