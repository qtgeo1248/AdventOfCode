import pprint
import math

pp = pprint.PrettyPrinter()

def main():
    f = open("tests/test.txt")

    scanners = []
    curScanner = None
    for line in f:
        if len(line) > 1:
            if line[4] == 's':
                if curScanner is not None:
                    scanners.append(curScanner)
                curScanner = []
            elif len(line) > 1:
                coord = line.rstrip().split(",")
                curScanner.append(tuple([int(coord[i]) for i in range(len(coord))]))
    pp.pprint(scanners)

    print("Answer: ")
    f.close()

if __name__ ==  "__main__":
    main()