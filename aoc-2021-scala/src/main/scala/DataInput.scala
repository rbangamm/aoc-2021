import scala.io.Source
import scala.annotation.targetName
import java.io.File
import java.nio.file.{Files, Paths}
import scala.collection.JavaConverters._

object DataInput:
  def fromResource(name: String): Seq[String] = Source.fromResource(name).getLines.toVector