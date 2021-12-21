import pprint

pp = pprint.PrettyPrinter()

def main():
    f = open("adapters.txt")
    jolts = []
    for line in f:
        jolts.append(int(line.rstrip()))
    jolts.sort()

    # Num Possible for all chains that end in that particular joltage
    numPoss = [0 for _ in range(jolts[len(jolts) - 1] + 1)]
    numPoss[0] = 1
    for i in range(len(jolts)):
        for diff in range(1, 4):
            if jolts[i] - diff >= 0:
                numPoss[jolts[i]] += numPoss[jolts[i] - diff]

    print("Answer: " + str(numPoss[jolts[len(jolts) - 1]]))
    f.close()

if __name__ ==  "__main__":
    main()