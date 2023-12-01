import pprint

pp = pprint.PrettyPrinter()

# line = f.readline().rstrip()

def isWord(line, i):
    words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for idx, word in enumerate(words):
        if i + len(word) <= len(line) and line[i:(i + len(word))] == word:
            return idx + 1
    return None

def main():
    f = open("calibration.txt")
    tot = 0
    for line in f:
        line = line.rstrip()
        cur = 0
        for i in range(len(line)):
            if line[i].isdigit():
                cur += 10 * int(line[i])
                break
            attempt = isWord(line, i)
            if attempt is not None:
                cur += 10 * attempt
                break
        for i in range(len(line)):
            if line[-(i + 1)].isdigit():
                cur += int(line[-(i + 1)])
                break
            attempt = isWord(line, len(line) - i - 1)
            if attempt is not None:
                cur += attempt
                break
        tot += cur
        # print(cur)
    print(tot)

if __name__ == "__main__":
    main()