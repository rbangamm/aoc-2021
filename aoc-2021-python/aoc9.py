visited = set()
def dfs(i, j, grid):
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    ret = 1
    visited.add((i, j))
    for x, y in dirs:
        if (i+x, j+y) not in visited and i+x < len(grid) - 1 and j+y < len(grid[0]) - 1 and i+x >= 1 and j+y >= 1 and grid[i+x][j+y] != 9:
            ret += dfs(i+x, j+y, grid)
    return ret

def part1():
    lines = []
    with open("input.txt") as file:
        lines = file.readlines()
        lines = [line.strip() for line in lines if len(line.strip()) > 0]
    total = 0
    lines = [[int(c) for c in line] for line in lines]
    lines = [[float("inf") for i in range(len(lines[0]))]] + lines + [[float("inf") for i in range(len(lines[0]))]]
    basins = []
    for i in range(len(lines)):
        lines[i] = [float("inf")] + lines[i] + [float("inf")]
    global visited
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for i in range(1, len(lines) - 1):
        for j in range(1, len(lines[i]) - 1):
            ok = True
            for x, y in dirs:
              if lines[i+x][j+y] <= lines[i][j]:
                  ok = False
                  break
            if not ok:
                continue
            size = dfs(i, j, lines)
            if size != 0:
                basins.append(size)
            visited = set()
    basins.sort()
    print(basins[-1] * basins[-2] * basins[-3])
part1()