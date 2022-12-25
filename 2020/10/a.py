import pprint

pp = pprint.PrettyPrinter()

def main():
    f = open("adapters.txt")
    diffs = [0, 0, 0, 0]
    jolts = []
    for line in f:
        jolts.append(int(line.rstrip()))
    jolts.sort()

    for i in range(len(jolts) + 1):
        if i == 0:
            diffs[jolts[i]] += 1
        elif i == len(jolts):
            diffs[3] += 1
        else:
            diff = jolts[i] - jolts[i - 1]
            if diff == 1 or diff == 3:
                diffs[diff] += 1

    print("Answer: " + str(diffs[3] * diffs[1]))
    f.close()

if __name__ ==  "__main__":
    main()