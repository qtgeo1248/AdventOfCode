import pprint

pp = pprint.PrettyPrinter()
numPos = 7
numDigits = 10

# The ones with only one possible length, so can make definite claims
easy = [
    [False, False, True, False, False, True, False],
    [True, False, True, False, False, True, False],
    [False, True, True, True, False, True, False]]

# Decoding
decoders = [
    {0, 1, 2, 4, 5, 6},
    {2, 5},
    {0, 2, 3, 4, 6},
    {0, 2, 3, 5, 6},
    {1, 2, 3, 5},
    {0, 1, 3, 5, 6},
    {0, 1, 3, 4, 5, 6},
    {0, 2, 5},
    {0, 1, 2, 3, 4, 5, 6},
    {0, 1, 2, 3, 5, 6}]

'''
My Positions 
   0
  1 2
   3
  4 5
   6
'''

def init(start):
    wires = []
    for _ in range(numPos):
        row = set()
        if start:
            for j in range(numPos):
                row.add(j)
        wires.append(row)
    return wires

# Removes the possibilities of positions of wires with 1, 4, and 7 clues
def rem_easy(wires, posses, pos, tester):
    for i in range(numPos):
        if ((tester in wires[pos]) ^ (easy[tester][i])) and i in posses[pos]:
            posses[pos].remove(i)

def rewire(rewiring, hint):
    positions = set()
    for pos in hint:
        positions.add(rewiring[pos])
    return positions

def other(poss, j):
    for i in poss:
        if i != j:
            return i

def getTrials(posses, i, trials, done):
    if i < len(posses):
        if i in done:
            return getTrials(posses, i + 1, trials, done)
        newTrials = []
        newDone = done.copy()
        done.append(i)
        for j in posses[i]:
            for trial in trials:
                newTrial = trial.copy()
                newTrial[i] = j
                for newI in range(len(newTrial)):
                    if newI != i and j in posses[newI]:
                        newDone.append(newI)
                        newTrial[newI] = other(posses[newI], j)
                newTrials.append(newTrial)
        return getTrials(posses, i + 1, newTrials, newDone)
    return trials

# Each thing only has pairs left, so deduces it one by one
def remHard(posses, hints):
    # pp.pprint(posses)
    trials = getTrials(posses, 0, [[None for _ in range(len(posses))]], [])
    # pp.pprint(trials)
    for trial in trials:
        isValid = True
        for hint in hints:
            untangled = rewire(trial, hint)
            if untangled not in decoders:
                isValid = False
        if isValid:
            return trial

def digit(positions):
    for i in range(numDigits):
        if positions == decoders[i]:
            return i

def main():
    f = open("displays.txt")
    ans = 0
    for line in f:
        hints = []
        wires = init(False)
        code = line.split(" ")
        tokidx = 0
        while code[tokidx] != "|":
            tok = code[tokidx]
            hint = set()
            for j in range(len(tok)):
                wires[ord(tok[j]) - ord('a')].add(len(tok) - 2)
                hint.add(ord(tok[j]) - ord('a'))
            if len(hint) != 2 and len(hint) != 3 and len(hint) != 4 and len(hint) != 7:
                hints.append(hint)
            tokidx += 1
        tokidx += 1

        # pp.pprint(wires)
        # pp.pprint(hints)
        posses = init(True)
        for i in range(numPos):
            for j in range(3):
                rem_easy(wires, posses, i, j)
        rewiring = remHard(posses, hints)
        # pp.pprint(rewiring)

        output = 0
        while tokidx < len(code):
            tok = code[tokidx].rstrip()
            positions = set()
            for i in range(len(tok)):
                positions.add(rewiring[ord(tok[i]) - ord('a')])
            output = 10 * output + digit(positions)
            tokidx += 1
        ans += output
    print("Answer: " + str(ans))

if __name__ == "__main__":
    main()