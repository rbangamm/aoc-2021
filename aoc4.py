import sys

def checkCol(col, board):
    for row in board:
        if row[col] != -1:
            return False
    return True

def checkRow(row, board):
    for col in board[row]:
        if col != -1:
            return False
    return True

def checkBoard(num, board):
    done = False
    for i in range(len(board)):
        for j in range(len(board[i])):
            if num == board[i][j]:
                board[i][j] = -1
                done = checkRow(i, board) or checkCol(j, board) or done
                if done:
                    print("here!!", board, num) 
    #print(num, board)
    return done

def calcUnmarkedNums(board):
    total = 0
    for row in board:
        for col in row:
            if col != -1:
                total += col
    return total    

def part1():
    with open("input.txt") as file:
        lines = file.readlines()
        lines = [line.strip() for line in lines if len(line.strip()) > 0]
    drawn = [int(num) for num in lines[0].split(",")]
    boards = []
    for i in range(1, len(lines), 5):
        board = []
        for j in range(5):
            board.append([int(num) for num in lines[i + j].split()])
        boards.append(board)
    total = 0
    for d in drawn:
        breakFlag = False
        for i in range(len(boards)):
            if checkBoard(d, boards[i]):
                breakFlag = True
                total = calcUnmarkedNums(boards[i])
                break
        if breakFlag:
            break
    print(d, total)
    print(d * total)

def part2():
    with open("input.txt") as file:
        lines = file.readlines()
        lines = [line.strip() for line in lines if len(line.strip()) > 0]
    drawn = [int(num) for num in lines[0].split(",")]
    boards = []
    for i in range(1, len(lines), 5):
        board = []
        for j in range(5):
            board.append([int(num) for num in lines[i + j].split()])
        boards.append(board)
    total = 0
    boardChecked = [False for i in range(len(boards))]
    finishOrder = []
    for d in drawn:
        for i in range(len(boards)):
            if checkBoard(d, boards[i]) and not boardChecked[i]:
                finishOrder.append((d, [[col for col in row] for row in boards[i]]))
                boardChecked[i] = True

    d, board = finishOrder.pop()
    print(d, calcUnmarkedNums(board))
    print(d * calcUnmarkedNums(board))

part2()