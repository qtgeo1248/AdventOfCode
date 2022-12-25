import pprint

pp = pprint.PrettyPrinter()

def getPrior(e):
    return ord(e) - ord('A') + 27 if ord(e) <= ord('Z') else ord(e) - ord('a') + 1

def main():
    f = open("rucksacks.txt")
    lines = f.readlines()
    i = 0
    priors = 0
    while i < len(lines):
        first = set(lines[i].strip())
        second = set(lines[i + 1].strip())
        third = set(lines[i + 2].strip())
        for e in first.intersection(second).intersection(third):
            priors += getPrior(e)
        i += 3
    print(priors)


if __name__ == "__main__":
    main()