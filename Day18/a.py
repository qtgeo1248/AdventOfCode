import pprint
import math

pp = pprint.PrettyPrinter()

# Beginning of line is '['
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
    if type(snailSum) is int:
        return snailSum + r
    snailSum[idx] = bringDown(snailSum[idx], r, idx)
    return snailSum

# It will go down to every child and check if you need to explode. It will pass
# information up from parent to parent so the necessary parent passes down the
# things needed to be edited.
# Returns ([l, r], isExploded)
# [l, r] is None if and only if isExploded is False
# l being None means that the changes for the left number of the exploding pair
# have been propgated (by you, or your child already)
def explode(snailSum, depth):
    # pp.pprint(snailSum)
    if type(snailSum) is int:
        return (None, False)
    if depth < 4:
        for idx in range(2):
            # See if your child needs to explode
            (child, isExploded) = explode(snailSum[idx], depth + 1)
            if isExploded:
                output = [child[0], child[1]]
                if depth == 3:
                    snailSum[idx] = 0
                # Note that if you are seeing if your left child exploded, you
                # need to edit the right branch, and vice verse
                other = int(not idx)
                if child[other] is not None:
                    # This being non-None means that the child has exploded, but
                    # changes haven't been propogated yet
                    snailSum[other] = bringDown(snailSum[other], child[other], idx)
                    output[other] = None
                return (output, isExploded)
        return (None, False)
    if depth == 4:
        return ([snailSum[0], snailSum[1]], True)

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