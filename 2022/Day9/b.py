import pprint

pp = pprint.PrettyPrinter()

def moveHead(head, dir):
    if dir == "R":
        head[0] += 1
    elif dir == "L":
        head[0] -= 1
    elif dir == "U":
        head[1] += 1
    else:
        head[1] -= 1

def moveTails(head, tail):
    if abs(head[0] - tail[0]) > 1 or abs(head[1] - tail[1]) > 1:
        if head[1] != tail[1]:
            tail[1] += 1 if head[1] > tail[1] else -1
        if head[0] != tail[0]:
            tail[0] += 1 if head[0] > tail[0] else -1

def main():
    f = open("motions.txt")

    totalPos = set()
    rope = [[0, 0] for _ in range(10)]
    totalPos.add((0, 0))
    for line in f:
        line = line.strip().split(" ")
        for _ in range(int(line[1])):
            moveHead(rope[0], line[0])
            for i in range(1, 10):
                moveTails(rope[i - 1], rope[i])
            totalPos.add((rope[9][0], rope[9][1]))

    print(len(totalPos))

if __name__ == "__main__":
    main()
