import sys

def part1():
    last = None
    total = 0
    for line in sys.stdin:
        if last is None:
            last = int(line.rstrip("\n"))
        else:
            num = int(line.rstrip("\n"))
            if num > last:
                total += 1
            last = num

    print(total)

def part2():
    total = 0
    window = []
    for line in sys.stdin:
        if len(window) < 3:
            window.append(int(line.rstrip("\n")))
        else:
            num = int(line.rstrip("\n"))
            if window[1] + window[2] + num > sum(window):
                total += 1
            window.pop(0)
            window.append(num)

    print(total)

part2()
