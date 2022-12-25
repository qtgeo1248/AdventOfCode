import pprint

pp = pprint.PrettyPrinter()

# line = f.readline().rstrip()

def main():
    f = open("text.txt")
    cur = 0
    max1 = 0
    max2 = 0
    max3 = 0
    for line in f:
        if line == "\n":
            if cur >= max1:
                max3 = max2
                max2 = max1
                max1 = cur
            elif cur >= max2:
                max3 = max2
                max2 = cur
            elif cur >= max3:
                max3 = cur
            cur = 0
        else:
            cur += int(line.strip())
    print(max1 + max2 + max3)

if __name__ == "__main__":
    main()