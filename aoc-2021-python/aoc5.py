import collections
def part1():
    lines = []
    with open("input.txt") as file:
        lines = file.readlines()
        lines = [line.strip() for line in lines if len(line.strip()) > 0]
    lines = [line.split(" -> ") for line in lines]
    lines = [(int(line[0].split(",")[0]), int(line[0].split(",")[1]), int(line[1].split(",")[0]), int(line[1].split(",")[1])) for line in lines]
    table = collections.defaultdict(int)
    maxX = float("-inf")
    maxY = float("-inf")
    for x1, y1, x2, y2 in lines:
        maxX = max(max(x1, maxX), x2)
        maxY = max(max(y1, maxY), y2)
        if x1 == x2:
            start = min(y1, y2)
            end = max(y1, y2)
            for i in range(start, end + 1):
                table[(x1, i)] += 1
        elif y1 == y2:
            start = min(x1, x2)
            end = max(x1, x2)
            for i in range(start, end + 1):
                table[(i, y1)] += 1
    total = 0
    for i in range(maxY + 1):
        for j in range(maxX + 1):
            if table[(j, i)] >= 2:
                total += 1
    print(total)

def part2():
    lines = []
    with open("input.txt") as file:
        lines = file.readlines()
        lines = [line.strip() for line in lines if len(line.strip()) > 0]
    lines = [line.split(" -> ") for line in lines]
    lines = [(int(line[0].split(",")[0]), int(line[0].split(",")[1]), int(line[1].split(",")[0]), int(line[1].split(",")[1])) for line in lines]
    table = collections.defaultdict(int)
    maxX = float("-inf")
    maxY = float("-inf")
    for x1, y1, x2, y2 in lines:
        maxX = max(max(x1, maxX), x2)
        maxY = max(max(y1, maxY), y2)
        if x1 == x2:
            start = min(y1, y2)
            end = max(y1, y2)
            for i in range(start, end + 1):
                table[(x1, i)] += 1
        elif y1 == y2:
            start = min(x1, x2)
            end = max(x1, x2)
            for i in range(start, end + 1):
                table[(i, y1)] += 1
        elif abs(x1 - x2) == abs(y1 - y2):
            diff = abs(x1 - x2)
            diffX = (x2 - x1) // diff
            diffY = (y2 - y1) // diff
            for i in range(diff + 1):
                table[(x1 + diffX * i, y1 + diffY * i)] += 1

    total = 0
    for i in range(maxY + 1):
        for j in range(maxX + 1):
            if table[(j, i)] > 0:
                total += 1 if table[(j, i)] >= 2 else 0
    print(total)

part2()