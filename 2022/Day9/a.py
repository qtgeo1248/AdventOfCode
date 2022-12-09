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
    head = [0, 0]
    tail = [0, 0]
    totalPos.add((0, 0))
    for line in f:
        line = line.strip().split(" ")
        for _ in range(int(line[1])):
            moveHead(head, line[0])
            moveTails(head, tail)
            totalPos.add((tail[0], tail[1]))

    print(len(totalPos))

if __name__ == "__main__":
    main()