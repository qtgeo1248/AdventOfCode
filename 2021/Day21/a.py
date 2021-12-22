import pprint
import math

pp = pprint.PrettyPrinter()
maxScore = 1000

def main():
    f = open("positions.txt")
    spots = []
    for line in f:
        spots.append(int(line.rstrip().split(": ")[1]))

    scores = [0, 0]
    ans = None
    die = 1
    player = 0
    rolled = 0
    while ans is None:
        spots[player] += die + ((die % 100) + 1) + (((die + 1) % 100) + 1)
        spots[player] = ((spots[player] - 1) % 10) + 1
        scores[player] += spots[player]
        die = ((die + 2) % 100) + 1
        rolled += 3
        if scores[player] >= 1000:
            ans = scores[not player] * rolled
        player = not player

    print("Answer: " + str(ans))
    f.close()

if __name__ ==  "__main__":
    main()