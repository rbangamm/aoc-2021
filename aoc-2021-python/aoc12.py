import collections

def dfs(graph, node, paths, small, smallCount, visited=set(), path=[]):
    path.append(node)

    if node == "end":
        paths.add(tuple(path[:]))
        path.pop()
        return

    if node.upper() != node and node != small:
        visited.add(node)
    
    if node == small:
        smallCount += 1
    
    for neighbour in graph[node]:
        if (neighbour != small and neighbour not in visited) or (neighbour == small and smallCount < 2):
            dfs(graph, neighbour, paths, small, smallCount, visited, path)

    if node == small:
        smallCount -= 1

    if node in visited:
        visited.remove(node)
    path.pop()

lines = []
with open("input.txt") as file:
    lines = file.readlines()
    lines = [line.strip() for line in lines if len(line.strip()) > 0]

graph = collections.defaultdict(list)
smallSet = set()
for line in lines:
    src, dest = line.split("-")
    if src.upper() != src:
        smallSet.add(src)
    if dest.upper() != dest:
        smallSet.add(dest)
    graph[src].append(dest)
    graph[dest].append(src)

visited = set()
paths = set()

for small in smallSet:
    if small not in ["start", "end"]:
        dfs(graph, "start", paths, small, 0)
        visited = set()

print(len(paths))