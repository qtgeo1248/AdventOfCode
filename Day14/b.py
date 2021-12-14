import pprint

steps = 40

def main():
    pp = pprint.PrettyPrinter()
    f = open("polymer.txt")
    rules = {}
    linePolymer = f.readline().rstrip()
    polymer = {}
    for i in range(len(linePolymer) - 1):
        pair = str(linePolymer[i]) + str(linePolymer[i + 1])
        if pair not in polymer.keys():
            polymer[pair] = 1
        else:
            polymer[pair] += 1
    f.readline()

    for line in f:
        parts = line.rstrip().split(" -> ")
        rules[parts[0]] = parts[1]

    for _ in range(steps):
        newPoly = {}
        for (pair, val) in polymer.items():
            if pair in rules.keys():
                newPairs = [str(pair[0]) + str(rules[pair]),
                            str(rules[pair]) + str(pair[1])]
                for newPair in newPairs:
                    if newPair not in newPoly:
                        newPoly[newPair] = val
                    else:
                        newPoly[newPair] += val
            else:
                if pair not in newPoly:
                    newPoly[pair] = val
                else:
                    newPoly[pair] += val
        polymer = newPoly
        # pp.pprint(polymer)
    counts = {}
    for (pair, val) in polymer.items():
        for char in pair:
            if char not in counts.keys():
                counts[char] = val
            else:
                counts[char] += val

    counts[linePolymer[0]] += 1
    counts[linePolymer[len(linePolymer) - 1]] += 1

    for (char, val) in counts.items():
        counts[char] = val // 2

    sortedLetters = list(counts.items())
    sortedLetters.sort(key = lambda x: x[1])
    pp.pprint(sortedLetters)
    ans = sortedLetters[len(sortedLetters) - 1][1] - sortedLetters[0][1]

    print("Answer: " + str(ans))
    f.close()

if __name__ ==  "__main__":
    main()