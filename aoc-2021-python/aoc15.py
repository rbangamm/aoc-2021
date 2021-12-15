import collections
import heapq
lines = []
with open("input.txt") as file:
    lines = file.readlines()
    lines = [line.strip() for line in lines if len(line.strip()) > 0]
for i in range(len(lines)):
    lines[i] = [int(c) for c in lines[i]]

rows = len(lines)
cols = len(lines[0])
for i in range(len(lines)):
    for j in range(cols * 4):
        tmp = lines[i][len(lines[i])-cols] + 1
        if tmp == 10:
            tmp = 1
        lines[i].append(tmp)
for i in range(rows * 4):
    row = [num + 1 for num in lines[len(lines)-rows]]
    for j in range(len(row)):
        if row[j] == 10:
            row[j] = 1
    lines.append(row)
rows *= 5
cols *= 5
heap = [(0, 0, 0)]
visited = set()
dist = [[float("inf") for j in range(len(lines[0]))] for i in range(len(lines))]
dist[0][0] = 0

while len(heap) > 0:

    d, i, j = heapq.heappop(heap)

    if (i, j) in visited:
        continue

    visited.add((i, j))

    dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]

    for x, y in dirs:
        if (i+x, j+y) in visited:
            continue
        if 0 <= i + x < len(lines) and 0 <= j + y < len(lines[0]):
            tmp = dist[i][j] + lines[i+x][j+y]
            if tmp < dist[i+x][j+y]:
                dist[i+x][j+y] = tmp
                heapq.heappush(heap, (tmp, i+x, j+y))

print(dist[rows-1][cols-1])