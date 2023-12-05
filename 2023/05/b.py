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
            for i in range(len(elems) // 2):
                seeds.add((int(elems[2 * i]), int(elems[2 * i]) + int(elems[2 * i + 1])))
        elif len(line) == 1:
            while len(seeds) > 0:
                newSeeds.add(seeds.pop())
            seeds = newSeeds
            newSeeds = set()
        elif line[-2] != ":":
            [toStart, fromStart, fromLen] = [int(elem) for elem in line.rstrip().split(" ")]
            fromEnd = fromStart + fromLen
            temp = set()
            while len(seeds) > 0:
                (seedStart, seedEnd) = seeds.pop()
                if fromStart <= seedStart and seedStart < fromEnd:
                    newSeeds.add((toStart + seedStart - fromStart, toStart + min(seedEnd, fromEnd) - fromStart))
                    if seedEnd > fromEnd:
                        temp.add((fromEnd, seedEnd))
                elif seedStart < fromStart and fromStart < seedEnd:
                    newSeeds.add((toStart, toStart + min(seedEnd, fromEnd) - fromStart))
                    temp.add((seedStart, fromStart))
                    if seedEnd > fromEnd:
                        temp.add((fromEnd, seedEnd))
                else:
                    temp.add((seedStart, seedEnd))
            seeds = temp
    print(min(seeds)[0])

if __name__ == "__main__":
    main()
