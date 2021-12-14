import collections

def totalSum(n):
    return n * (n + 1) // 2

def part1():
    lines = []
    with open("input.txt") as file:
        lines = file.readlines()
        lines = [line.strip() for line in lines if len(line.strip()) > 0]
    nums = [int(num) for num in lines[0].split(",")]
    _max = max(nums)
    ans = float("inf")
    for i in range(_max + 1):
        total = 0
        for num in nums:
            total += totalSum(abs(num - i))
        ans = min(ans, total)
    print(ans)

part1()