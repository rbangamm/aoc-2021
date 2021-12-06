import collections
def part1():
    lines = []
    with open("input.txt") as file:
        lines = file.readlines()
        lines = [line.strip() for line in lines if len(line.strip()) > 0]
    fish = [int(num) for num in lines[0].split(",")]
    table = collections.defaultdict(int)
    for f in fish:
        table[f] += 1
    total = len(fish)
    for i in range(256):
        if table[i] >= 1:
            total += table[i]
            table[i+9] += table[i]
            table[i+7] += table[i]
    print(total)

part1()