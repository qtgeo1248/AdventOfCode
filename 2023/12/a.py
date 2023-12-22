import pprint

pp = pprint.PrettyPrinter(width=150)

# line = f.readline().rstrip()

def trial(idx, questions, line, hints):
    if idx == len(questions):
        curGroups = []
        curGroup = 0
        for c in line:
            if c == '#':
                curGroup += 1
            elif curGroup != 0:
                curGroups.append(curGroup)
                curGroup = 0
        if curGroup != 0:
            curGroups.append(curGroup)
        return 1 if curGroups == hints else 0
    tot = 0
    for new in ['.', '#']:
        line[questions[idx]] = new
        tot += trial(idx + 1, questions, line, hints)
    return tot

def numArrange(line, hints):
    questions = []
    for i in range(len(line)):
        if line[i] == '?':
            questions.append(i)
    return trial(0, questions, line, hints)

def main():
    f = open("springs.txt")

    numPoss = 0
    for line in f:
        [spring, hints] = line.rstrip().split(" ")
        numPoss += numArrange([c for c in spring], [int(c) for c in hints.split(",")])

    pp.pprint(numPoss)

if __name__ == "__main__":
    main()
