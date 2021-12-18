import pprint

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
        bringDown(snailSum[idx], r)

# Returns ((l, r), )
# isExploded is return value to help you keep exploding int parent, while
# checking if child is None is for seeing if you need to edit
def explode(snailSum, depth):
    pp.pprint(snailSum)
    if type(snailSum) is int:
        return (None, False)
    else:
        if depth < 4:
            (child, isExploded) = explode(snailSum[0], depth + 1)
            if isExploded:
                if child is not None:
                    if depth == 3:
                        snailSum[0] = 0
                    if child[1] is not None:
                        if type(snailSum[1]) is int:
                            snailSum[1] += child[1]
                        else: 
                            bringDown(snailSum[1], child[1], 0)
                    return ((child[0], None), isExploded)
                return (child, isExploded)
            else: 
                (child, isExploded) = explode(snailSum[1], depth + 1)
                if isExploded:
                    if child is not None:
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

def reduced(snailSum):
    while explode(snailSum, 0)[1]:
        snailSum = snailSum
    return snailSum

def main():
    f = open("tests/testExplode5.txt")

    addends = []
    for line in f:
        line = line.rstrip()
        addends.append(process(line)[0])

    explode(addends[0], 0)
    pp.pprint(addends[0])
    
    # while len(addends) > 1:
    #     left = addends.pop(0)
    #     right = addends[0]
    #     snailSum = [left, right]
    #     addends[0] = reduced(snailSum)

    # pp.pprint(addends)

    print("Answer: ")
    f.close()

if __name__ ==  "__main__":
    main()