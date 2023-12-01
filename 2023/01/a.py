import pprint

pp = pprint.PrettyPrinter()

# line = f.readline().rstrip()

def main():
    f = open("calibration.txt")
    tot = 0
    for line in f:
        cur = 0
        line = line.rstrip()
        for c in line:
            if c.isdigit():
                cur += 10 * int(c)
                break
        for i in range(len(line)):
            if line[-(i + 1)].isdigit():
                cur += int(line[-(i + 1)])
                break
        tot += cur
    print(tot)

if __name__ == "__main__":
    main()