lines = []
with open("input.txt") as file:
    lines = file.readlines()
    lines = [line.strip() for line in lines if len(line.strip()) > 0]

binString = bin(int(lines[0], 16))[2:]
if len(binString) % 4 > 0:
    binString = (4 - len(binString) % 4)  * "0" + binString
totalSum = 0
def parseString(binString, i, numPackets=float("inf")):
    print(binString)
    global totalSum
    curPackets = 0
    while i < len(binString):
        version = int(binString[i:i+3], 2)
        typeId = int(binString[i+3:i+6], 2)
        print(binString[i:i+3], version, i)
        if typeId == 4:
            i += 6
            num = 0
            while True:
                if binString[i] == "0":
                    num += int(binString[i+1:i+5], 2)
                    i += 5
                    break
                else:
                    num += int(binString[i+1:i+5], 2)
                    num <<= 4
                i += 5
            while i < len(binString) and binString[i] == "0":
                i += 1
            totalSum += version
            curPackets += 1
        else:
            if binString[i+6] == "0":
                size = int(binString[i+7:i+22], 2)
                while i + 22 + size < len(binString) and binString[i+22+size] == "0":
                    size += 1
                parseString(binString[22:22+size], 0)
                totalSum += version
                i += 22+size
                curPackets += 1
            else:
                numPackets = int(binString[i+7:i+18], 2)
                y = parseString(binString[i+18:], 0, numPackets)
                totalSum += version
                i += y
                curPackets += 1
        if curPackets == numPackets:
            return i
    return i



parseString(binString, 0)

print(totalSum)