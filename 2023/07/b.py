from collections import Counter
import pprint

pp = pprint.PrettyPrinter(width=150)

# line = f.readline().rstrip()

cardMap = {'A': 12, 'K': 11, 'Q': 10, 'T': 9, '9': 8, '8': 7, '7': 6, '6': 5, '5': 4, '4': 3, '3': 2, '2': 1, 'J': 0}

def getType(card):
    counter = Counter(card)
    count = list(counter.items())
    count.sort(key=lambda x: -x[1])

    highest, second = None, None

    if 'J' in counter:
        if count[0][0] != 'J':
            highest = count[0][1] + counter['J']
            
        elif len(count) > 1:
            highest = count[1][1] + counter['J']
        else:
            highest = counter['J']

        if len(count) > 1 and count[1][0] != 'J':
            second = count[1][1]
        elif len(count) > 2:
            second = count[2][1]
        else:
            second = 0
    else:
        highest = count[0][1]
        second = (count[1][1] if len(count) > 1 else 0)

    if highest == 5:
        return 6
    elif highest == 4:
        return 5
    elif highest == 3:
        return 3 + (1 if second == 2 else 0)
    elif highest == 2:
        return 1 + (1 if second == 2 else 0)
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
    # print(cards)
    cards.sort()
    ans = 0
    for i in range(len(cards)):
        ans += cards[i].bid * (i + 1)
    print(ans)

if __name__ == "__main__":
    main()
