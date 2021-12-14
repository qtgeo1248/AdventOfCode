import pprint

steps = 10

def main():
    pp = pprint.PrettyPrinter()
    f = open("polymer.txt")
    rules = {}
    polymer = f.readline().rstrip()
    f.readline()

    for line in f:
        parts = line.rstrip().split(" -> ")
        rules[parts[0]] = parts[1]

    for _ in range(steps):
        newPoly = ""
        for i in range(len(polymer)):
            newPoly += str(polymer[i])
            if i < len(polymer) - 1:
                pair = str(polymer[i]) + str(polymer[i + 1])
                if pair in rules.keys():
                    newPoly += str(rules[pair])
        pp.pprint(str(len(newPoly)))
        polymer = newPoly

    counts = {}
    for i in range(len(polymer)):
        if polymer[i] not in counts.keys():
            counts[polymer[i]] = 1
        else:
            counts[polymer[i]] += 1

    sortedLetters = list(counts.items())
    sortedLetters.sort(key = lambda x: x[1])
    pp.pprint(sortedLetters)
    ans = sortedLetters[len(sortedLetters) - 1][1] - sortedLetters[0][1]

    print("Answer: " + str(ans))
    f.close()

if __name__ ==  "__main__":
    main()