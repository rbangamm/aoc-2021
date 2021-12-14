def placeRows(grid, num, line):
    rows = []
    for i in range(num):
        rows.append(grid.pop())
    grid = grid[:line]
    grid = rows + grid
    return grid

def placeCols(grid, num, line):
    for i in range(len(grid)):
        cols = []
        for j in range(num):
            cols.append(grid[i].pop())
        grid[i] = grid[i][:line]
        grid[i] = cols + grid[i]
    return grid

def countMarks(grid):
    total = 0
    for row in grid:
        for col in row:
            total += 1 if col == '#' else 0
    return total

def prettyPrint(grid):
    for row in grid:
        print(''.join(row))

lines = []
with open("input.txt") as file:
    lines = file.readlines()
    lines = [line.strip() for line in lines if len(line.strip()) > 0]

maxX = 0
maxY = 0
ind = 0
points = []   
for i in range(len(lines)):
    if lines[i][0] == 'f':
        ind = i
        break
    x, y = lines[i].split(",")
    x = int(x)
    y = int(y)
    maxX = max(maxX, x)
    maxY = max(maxY, y)
    points.append((x, y))

grid = [['.' for x in range(maxX+1)] for y in range(maxY+1)]
for x, y in points:
    grid[y][x] = '#'
prettyPrint(grid)
print("")
for k in range(ind, len(lines)):
    instruction = lines[k].split()
    if instruction[2][0] == 'x':
        line = int(instruction[2].split("=")[1])
        for y in range(maxY + 1):
            for i in range(1, min(maxX - line, line) + 1):
                if grid[y][line-i] == '.':
                    grid[y][line - i] = '#' if grid[y][line+i] == '#' else '.'
        if maxX - line > line:
            diff = maxX - 2 * line
            grid = placeCols(grid, diff, line)
        else:
            for i in range(len(grid)):
                grid[i] = grid[i][:line]
        maxX = line - 1
    else:
        line = int(instruction[2].split("=")[1])
        for i in range(1, min(maxY - line, line) + 1):
            for x in range(maxX + 1):
                if grid[line - i][x] == '.':
                    grid[line - i][x] = '#' if grid[line+i][x] == '#' else '.'
        if maxY - line > line:
            diff = maxY - 2 * line
            grid = placeRows(grid, diff, line)
        else:
            grid = grid[:line]
        maxY = line - 1
prettyPrint(grid)
print(countMarks(grid))