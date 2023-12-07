from collections import Counter
import pprint

pp = pprint.PrettyPrinter(width=150)

# line = f.readline().rstrip()

cardMap = {'A': 12, 'K': 11, 'Q': 10, 'J': 9, 'T': 8, '9': 7, '8': 6, '7': 5, '6': 4, '5': 3, '4': 2, '3': 1, '2': 0}

def getType(card):
    count = list(Counter(card).items())
    count.sort(key=lambda x: -x[1])
    if count[0][1] == 5:
        return 6
    elif count[0][1] == 4:
        return 5
    elif count[0][1] == 3:
        return 3 + (1 if count[1][1] == 2 else 0)
    elif count[0][1] == 2:
        return 1 + (1 if count[1][1] == 2 else 0)
    return 0

class Card:
    def __init__(self, card, bid):
        self.card = card
        self.bid = bid
        self.type = getType(card)

    def __repr__(self):
        return str((self.card, self.bid, self.type))
    
    def __lt__(self, other):
        if self.type != other.type:
            return self.type < other.type
        for i in range(5):
            if cardMap[self.card[i]] != cardMap[other.card[i]]:
                return cardMap[self.card[i]] < cardMap[other.card[i]]
        return False

def main():
    f = open("cards.txt")

    cards = []
    
    for line in f:
        [card, bid] = line.rstrip().split()
        cards.append(Card(card, int(bid)))
    cards.sort()
    ans = 0
    for i in range(len(cards)):
        ans += cards[i].bid * (i + 1)
    print(ans)

if __name__ == "__main__":
    main()
