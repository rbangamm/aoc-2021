import sys

def findMostCommon(lines, o2=True):
    nums = []
    for line in lines:
        if len(nums) == 0:
            nums = [0] * len(line)
        for i in range(len(line)):
            nums[i] += 1 if line[i] == "1" else -1
    
    ret = ""

    for num in nums:
        if num < 0:
            ret += "0" if o2 else "1"
        elif num > 0:
            ret += "1" if o2 else "0"
        else:
            ret += "x"
    
    return ret

def part1():
    lines = []
    for line in sys.stdin:
        line = line.rstrip("\n")
        lines.append(line)
    originalLines = lines[:]
    count = len(lines[0])
    for i in range(count):
        num = findMostCommon(lines)
        filterNum = num[i]
        if filterNum == "x":
            filterNum = "1"
        lines = list(filter(lambda x : x[i] == filterNum, lines))
        if len(lines) == 1:
            break
    o2 = lines[0]
    lines = originalLines
    for i in range(count):
        num = findMostCommon(lines, False)
        filterNum = num[i]
        if filterNum == "x":
            filterNum = "0"
        lines = list(filter(lambda x : x[i] == filterNum, lines))
        if len(lines) == 1:
            break
    co2 = lines[0]
    print(int(o2, 2) * int(co2, 2))

part1()