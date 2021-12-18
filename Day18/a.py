import pprint
import math

pp = pprint.PrettyPrinter()

# Beginning of line is '['
# 
# Returns (arr, numProcessed)
def process(line):
    left = None
    if line[1] == '[':
        left = process(line[1:])
    elif '0' <= line[1] and line[1] <= '9':
        left = (ord(line[1]) - ord('0'), 1)
    right = None
    # Accounts for '[', the left processed, and the comma
    idxComma = 2 + left[1]
    if line[idxComma] == '[':
        right = process(line[idxComma:])
    elif '0' <= line[idxComma] and line[idxComma] <= '9':
        right = (ord(line[idxComma]) - ord('0'), 1)
    # pp.pprint((left, right))
    return ([left[0], right[0]], 3 + left[1] + right[1])

# Brings right side of explosion all the way down to the path, given idx
def bringDown(snailSum, r, idx):
    if type(snailSum[idx]) is int:
        snailSum[idx] += r
    else:
        bringDown(snailSum[idx], r, idx)

# Returns ((l, r), )
# isExploded is return value to help you keep exploding int parent, while
# checking if child is None is for seeing if you need to edit
def explode(snailSum, depth):
    # pp.pprint(snailSum)
    if type(snailSum) is int:
        return (None, False)
    else:
        if depth < 4:
            (child, isExploded) = explode(snailSum[0], depth + 1)
            if isExploded:
                if depth == 3:
                    snailSum[0] = 0
                if child[1] is not None:
                    if type(snailSum[1]) is int:
                        snailSum[1] += child[1]
                    else: 
                        bringDown(snailSum[1], child[1], 0)
                return ((child[0], None), isExploded)
            else: 
                (child, isExploded) = explode(snailSum[1], depth + 1)
                if isExploded:
                    if depth == 3:
                        snailSum[1] = 0
                    if child[0] is not None:
                        if type(snailSum[0]) is int:
                            snailSum[0] += child[0]
                        else: 
                            bringDown(snailSum[0], child[0], 1)
                    return ((None, child[1]), isExploded)
                else:
                    return (None, False)
        if depth == 4:
            return ((snailSum[0], snailSum[1]), True)

# Returns (splitArr, isSplit)
def split(snailSum):
    if type(snailSum) is int:
        if snailSum >= 10:
            return ([math.floor(snailSum / 2), math.ceil(snailSum / 2)], True)
        else:
            return (snailSum, False)
    else:
        left = split(snailSum[0])
        snailSum[0] = left[0]
        if not left[1]:
            right = split(snailSum[1])
            snailSum[1] = right[0]
            return (snailSum, right[1])
        else:
            return (snailSum, True)

def reduced(snailSum):
    notReduced = True
    while notReduced:
        if not explode(snailSum, 0)[1] and not split(snailSum)[1]:
            notReduced = False
    return snailSum

def magnitude(snailSum):
    if type(snailSum) is int:
        return snailSum
    else:
        return 3 * magnitude(snailSum[0]) + 2 * magnitude(snailSum[1])

def main():
    f = open("homework.txt")

    addends = []
    for line in f:
        line = line.rstrip()
        addends.append(process(line)[0])
    
    while len(addends) > 1:
        left = addends.pop(0)
        right = addends[0]
        snailSum = [left, right]
        addends[0] = reduced(snailSum)

    pp.pprint(addends[0])

    print("Answer: " + str(magnitude(addends[0])))
    f.close()

if __name__ ==  "__main__":
    main()