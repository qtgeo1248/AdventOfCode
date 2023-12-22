import pprint

pp = pprint.PrettyPrinter(width=200)

# line = f.readline().rstrip()

def trial(line, lineIdx, hints, hintsIdx, sumHints, brain):
    if hintsIdx == len(hints):
        for i in range(lineIdx, len(line)):
            if line[i] == '#':
                return 0
        return 1
    if (lineIdx, hintsIdx) in brain:
        return brain[(lineIdx, hintsIdx)]
    curHint = hints[hintsIdx]
    upper = len(line) - (sumHints - hints[hintsIdx] + len(hints) - hintsIdx - 1)
    tot = 0

    chars = {'#' : 0, '?' : 0, '.': 0}
    for j in range(lineIdx, lineIdx + curHint):
        chars[line[j]] += 1
    i = lineIdx
    while i + curHint <= upper and (i == 0 or line[i - 1] != '#'):
        if chars['.'] == 0 and i + curHint <= len(line) and (i + curHint == len(line) or line[i + curHint] != '#'):
            tot += trial(line, i + curHint + 1, hints, hintsIdx + 1, sumHints - curHint, brain)
        chars[line[i]] -= 1
        i += 1
        if i + curHint <= upper:
            chars[line[i + curHint - 1]] += 1
    brain[(lineIdx, hintsIdx)] = tot
    return tot

def numArrange(line, hints):
    brain = dict()
    return trial(line, 0, hints, 0, sum(hints), brain)

def main():
    f = open("springs.txt")

    numPoss = 0
    for line in f:
        [spring, hints] = line.rstrip().split(" ")
        spring += 4 * ("?" + spring)
        hints += 4 * ("," + hints)
        numPoss += numArrange([c for c in spring], [int(c) for c in hints.split(",")])

    pp.pprint(numPoss)

if __name__ == "__main__":
    main()
