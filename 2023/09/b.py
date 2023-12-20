import pprint

pp = pprint.PrettyPrinter(width=150)

# line = f.readline().rstrip()

def predict(history):
    allZeroes = True
    for hist in history:
        if hist != 0:
            allZeroes = False
    if allZeroes:
        return 0
    diffs = [history[i + 1] - history[i] for i in range(len(history) - 1)]
    return history[0] - predict(diffs)

def main():
    f = open("history.txt")

    histories = []
    for line in f:
        histories.append([int(sand) for sand in line.rstrip().split()])
    summ = 0
    for history in histories:
        summ += predict(history)
    print(summ)

if __name__ == "__main__":
    main()
