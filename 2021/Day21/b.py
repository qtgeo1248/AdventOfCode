import pprint
import math

pp = pprint.PrettyPrinter()
maxScore = 21

def prob(score):
    if score == 3:
        return 1
    if score == 4:
        return 3
    if score == 5:
        return 6
    if score == 6:
        return 7
    if score == 7:
        return 6
    if score == 8:
        return 3
    if score == 9:
        return 1

# Remember to use tuples, not lists
def universes(scores, spots, player):
    # pp.pprint((scores, spots, player))
    if scores[0] >= maxScore:
        return (1, 0)
    if scores[1] >= maxScore:
        return (0, 1)
    unis = [0, 0]
    for roll in range(3, 10):
        newScores = list(scores)
        newSpots = list(spots)
        newSpots[player] += roll
        newSpots[player] = ((newSpots[player] - 1) % 10) + 1
        newScores[player] += newSpots[player]
        child = universes(tuple(newScores), tuple(newSpots), not player)
        for i in range(len(unis)):
            unis[i] += prob(roll) * child[i]
    return tuple(unis)

def main():
    f = open("positions.txt")
    spots = []
    for line in f:
        spots.append(int(line.rstrip().split(": ")[1]))

    unis = universes((0, 0), tuple(spots), 0)
    ans = unis[0] if unis[0] > unis[1] else unis[1]

    print("Answer: " + str(ans))
    f.close()

if __name__ ==  "__main__":
    main()