// package day4

// import org.scalactic.Bool

// case class Coordinate(x: Int, y: Int)
// case class BingoNumber(coordinate: Coordinate, value: Int)

// sealed trait BingoLine:
//   def numbers: Seq[BingoNumber]
//   def isComplete(marker: Int = BingoGrid.DefaultMarked): Boolean = numbers.filterNot(_.value == marker).length == 1
// case class Row(override val numbers: Seq[BingoNumber]) extends BingoLine
// case class Column(override val numbers: Seq[BingoNumber]) extends BingoLine

// object BingoLine:
//   def apply(input: Seq[BingoNumber]): BingoLine =
//     if(input.map(_.coordinate.x).distinct.length == 1) then Row(input) else Column(input)


// case class BingoCard(grid : BingoGrid, isWinner: Boolean = false) {
//   lazy val totalUnmarked: Int = grid.unmarked().sum

//   def markBoard(value : Int) : BingoCard = {
//     grid.find(value) match {
//       case Some(found) =>
//         val updatedGrid = grid.set(found.coordinate)
//         copy(grid = updatedGrid, isWinner = checkWin(found.coordinate, updatedGrid))
//       case None =>  this
//     }
//   }

//   private def checkWin(coordinate : Coordinate, grid : BingoGrid) : Boolean = 
//     grid.row(coordinate.y).isComplete() || grid.column(coordinate.y).isComplete()  
// }

// object BingoCard:
//   def apply(input : Seq[Seq[Int]]) : BingoCard = {
//     for (i <- 0 to input.length - 1) {
//       for (j <- 0 to input(i).length - 1) {

//       }
//     }
//     BingoCard()
//   }

// case class BingoGrid(private val map :Map[Coordinate, Int]):
//   lazy val values: Seq[Int] = map.values.toSeq

//   def unmarked(marker: Int = BingoGrid.DefaultMarked): Seq[Int] = values.filterNot(_ == marker)

//   def find(value: Int): Option[BingoNumber] = map.find(_._2 == value).map(BingoNumber.apply)
//   def set(coordinate: Coordinate, marker: Int = BingoGrid.DefaultMarked): BingoGrid = copy(map = map.updated(coordinate, marker))

//   def row(y: Int): BingoLine = BingoLine(map.filter { case(coordinate, _) => coordinate.y == y }.map(BingoNumber.apply).toSeq)
//   def column(x: Int): BingoLine = BingoLine(map.filter { case(coordinate, _) => coordinate.x == x }.map(BingoNumber.apply).toSeq)

// object BingoGrid:
//   val DefaultMarked = -1

// case class BingoCardList(private val list : Seq[BingoCard]):
//   def setCards(number : Int) : BingoCardList = copy(list = list.map(_.markBoard(number)))
//   lazy val findWinner : Option[BingoCard] = list.find(_.isWinner) 

// object BingoCardList:
//   def apply(input : Seq[Seq[Seq[Int]]]) : BingoCardList = BingoCardList(list = input.map(BingoCard.apply))

// case class BingoGame(cards : BingoCardList) {
//   def play(number : Int) : BingoGame = copy(cards = cards.setCards(number))
//   lazy val winningSum : Int = {
//     cards.findWinner match {
//       case Some(found) => found.totalUnmarked
//       case None => -1
//     }
//   }
// }