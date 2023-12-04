import pprint

pp = pprint.PrettyPrinter(width=150)

# line = f.readline().rstrip()

def main():
    f = open("scratchcards.txt")
    ans = 0
    for line in f:
        line = line.rstrip().split(":")[1]
        res = line.split("|")
        winning = res[0].split(" ")
        have = res[1].split(" ")
        winningSet = set()
        havingSet = set()
        for num in winning:
            if num.isdigit():
                winningSet.add(num)
        for num in have:
            if num.isdigit():
                havingSet.add(num)
        numWinning = len(winningSet.intersection(havingSet))
        ans += 0 if numWinning == 0 else 1 << (numWinning - 1)
    print(ans)

if __name__ == "__main__":
    main()
