import pprint

pp = pprint.PrettyPrinter()

def getPrior(e):
    return ord(e) - ord('A') + 27 if ord(e) <= ord('Z') else ord(e) - ord('a') + 1

def main():
    f = open("rucksacks.txt")
    priors = 0
    for line in f:
        line = line.strip()
        first = set(line[0:(len(line) // 2)])
        second = set(line[(len(line) // 2):])
        for e in first.intersection(second):
            priors += getPrior(e)
    print(priors)

if __name__ == "__main__":
    main()