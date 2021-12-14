import collections
lines = []
with open("input.txt") as file:
    lines = file.readlines()
    lines = [line.strip() for line in lines if len(line.strip()) > 0]

cur = lines[0]
mapping = {}
for i in range(1, len(lines)):
    arr = lines[i].split(" -> ")
    mapping[arr[0]] = arr[1]

res = collections.defaultdict(int)
for a, b in zip(cur, cur[1:]):
    res[a + b] += 1
for i in range(40):
    new_dict = collections.defaultdict(int)
    for k in res:
        middle = mapping[k]
        new_dict[k[0] + middle] += res[k]
        new_dict[middle + k[1]] += res[k]
    res = new_dict

count = collections.defaultdict(int)
for k in res:
    count[k[0]] += res[k]
count[cur[-1]] += 1
res = [(k, count[k]) for k in count]
res.sort(key=lambda x : x[1])
print(res[-1][1] - res[0][1])