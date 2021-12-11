lines = []
with open("input.txt") as file:
    lines = file.readlines()
    lines = [line.strip() for line in lines if len(line.strip()) > 0]

lines = [[int(c) for c in line] for line in lines]
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

total = 0
print(lines)
for num in range(1000):
    flashCount = 0
    flashedSet = set()
    for j in range(len(lines)):
        for k in range(len(lines[0])):
            lines[j][k] += 1
            if lines[j][k] == 10:
                lines[j][k] = 0
                flashedSet.add((j, k))
                flashed = True
                total += 1
                flashCount += 1
    stack = list(flashedSet)
    while len(stack) > 0:
        i, j = stack.pop()
        for x, y in dirs:
            if 0 <= i + x < len(lines) and 0 <= j + y < len(lines[0]) and (i + x, j + y) not in flashedSet:
                lines[i+x][j+y] += 1
                if lines[i+x][j+y] == 10:
                    lines[i+x][j+y] = 0
                    flashedSet.add((i+x, j+y))
                    stack.append((i+x, j+y))
                    flashed = True
                    total += 1
                    flashCount += 1
    if (flashCount == len(lines) * len(lines[0])):
        print("Ans:", num+1)
        break
print(total)
