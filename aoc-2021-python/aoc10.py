lines = []
with open("input.txt") as file:
    lines = file.readlines()
    lines = [line.strip() for line in lines if len(line.strip()) > 0]

ENDS = {"}" : "{", ")" : "(", ">" : "<", "]" : "["}
scores = {"}" : 1197, ")" : 3, ">" : 25137, "]" : 57}
scoresStart = {"{" : 3, "(" : 1, "<" : 4, "[" : 2}
total = 0
totalScores = []
for line in lines:
    stack = []
    good = True
    for c in line:
        if c in ENDS and (len(stack) == 0 or stack[-1] != ENDS[c]):
            total += scores[c]
            good = False
            break
        elif c in ENDS and stack[-1] == ENDS[c]:
            stack.pop()
        else:
            stack.append(c)
    if good and len(stack) > 0:
        val = 0
        for i in range(len(stack) - 1, -1, -1):
            val = val * 5 + scoresStart[stack[i]]
        totalScores.append(val)
totalScores.sort()
print(totalScores[len(totalScores) // 2])