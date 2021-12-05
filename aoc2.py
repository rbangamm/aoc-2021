import sys

def part1():
    totalX = 0
    totalY = 0
    for line in sys.stdin:
        line = line.rstrip("\n")
        cmds = line.split(" ")
        num = int(cmds[1])
        if cmds[0] == "forward":
            totalX += num
        elif cmds[0] == "down":
            totalY += num
        else:
            totalY -= num

    print(totalX * totalY)

def part2():
    totalX = 0
    totalY = 0
    aim = 0
    for line in sys.stdin:
        line = line.rstrip("\n")
        cmds = line.split(" ")
        num = int(cmds[1])
        if cmds[0] == "forward":
            totalX += num
            totalY += aim * num
        elif cmds[0] == "down":
            aim += num
        else:
            aim -= num

    print(totalX * totalY)

part2()
