from collections import defaultdict
import pprint

pp = pprint.PrettyPrinter(width=150)

# line = f.readline().rstrip()

def main():
    f = open("scratchcards.txt")
    numCards = defaultdict(lambda: 0)
    for line in f:
        line = line.rstrip().split(":")
        rest = line[1].split("|")

        card = int(line[0].split(" ")[-1])
        numCards[card] += 1

        winning = rest[0].split(" ")
        have = rest[1].split(" ")
        winningSet = set()
        havingSet = set()
        for num in winning:
            if num.isdigit():
                winningSet.add(num)
        for num in have:
            if num.isdigit():
                havingSet.add(num)
        numWinning = len(winningSet.intersection(havingSet))
        for i in range(card + 1, card + numWinning + 1):
            numCards[i] += numCards[card]
    
    print(sum(numCards.values()))

if __name__ == "__main__":
    main()
