import pprint

pp = pprint.PrettyPrinter()

# line = f.readline().rstrip()

def main():
    f = open("calories.txt")
    cur = 0
    maxCur = 0
    for line in f:
        if line == "\n":
            maxCur = max(cur, maxCur)
            cur = 0
        else:
            cur += int(line.strip())
    print(maxCur)

if __name__ == "__main__":
    main()