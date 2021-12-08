def inSet(_set, s):
    for c in s:
        if c not in _set:
            return False
    return True

def commonChars(s, t):
    common = set()
    s = set(s)
    for c in t:
        if c in s:
            common.append(t)
    return common

def diffChars(s, t):
    s = set(s)
    t = set(t)
    res = []
    tmp = []
    for c in s:
        if c not in t:
            tmp.append(c)
    res.append(tmp)
    tmp = []
    for c in t:
        if c not in s:
            tmp.append(c)
    res.append(tmp)
    return res

def part1():
    lines = []
    with open("input.txt") as file:
        lines = file.readlines()
        lines = [line.strip() for line in lines if len(line.strip()) > 0]
    total = 0
    for i in range(0, len(lines)):
        mapping = {}
        rev_mapping = {}
        arr = lines[i].split(" | ")
        left = arr[0].strip().split()
        right = arr[1].strip().split()
        left.sort(key=len)
        mapping[1] = left[0]
        mapping[7] = left[1]
        mapping[4] = left[2]
        mapping[8] = left[-1]
        for s in left:
            if len(s) == 5 and inSet(s, mapping[1]):
                mapping[3] = s
                break
        for s in left:
            if len(s) == 6 and inSet(s, mapping[4]) and inSet(s, mapping[7]):
                mapping[9] = s
                break
        for s in left:
            if len(s) == 6 and inSet(s, mapping[7]) and not inSet(s, mapping[4]):
                mapping[0] = s
                break
        for s in left:
            if len(s) == 6 and not inSet(s, mapping[7]) and not inSet(s, mapping[4]):
                mapping[6] = s
                break
        remaining = []
        for s in left:
            if len(s) == 5 and not inSet(s, mapping[1]):
                remaining.append(s)
        
        res = diffChars(remaining[0], mapping[3])
        if inSet(mapping[4], res[0][0]):
            mapping[5] = remaining[0]
            mapping[2] = remaining[1]
        else:
            mapping[5] = remaining[1]
            mapping[2] = remaining[0]
        for key in mapping:
            v = [c for c in mapping[key]]
            v.sort()
            rev_mapping[''.join(v)] = key
        num = 0
        for t in right:
            t = [c for c in t]
            t.sort()
            num *= 10
            num += rev_mapping[''.join(t)]
        total += num

    print(total)

part1()