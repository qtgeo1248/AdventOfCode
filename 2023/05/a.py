import pprint

pp = pprint.PrettyPrinter(width=150)

# line = f.readline().rstrip()

def main():
    f = open("seeds.txt")
    seeds = set()
    newSeeds = set()
    for line in f:
        if line[0:6] == "seeds:":
            elems = line.rstrip().split(": ")[1].split(" ")
            for seed in elems:
                seeds.add(int(seed))
        elif len(line) == 1:
            while len(seeds) > 0:
                newSeeds.add(seeds.pop())
            seeds = newSeeds
            newSeeds = set()
        elif line[-2] != ":":
            [toStart, fromStart, fromLen] = [int(elem) for elem in line.rstrip().split(" ")]
            temp = set()
            while len(seeds) > 0:
                seed = seeds.pop()
                if fromStart <= seed and seed < fromStart + fromLen:
                    newSeeds.add(toStart + (seed - fromStart))
                else:
                    temp.add(seed)
            seeds = temp
    print(min(seeds))

if __name__ == "__main__":
    main()
