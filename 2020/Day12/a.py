import pprint

pp = pprint.PrettyPrinter()
numDirs = 4
N = 0
E = 1
S = 2
W = 3

def actToDir(act):
    if act == 'N':
        return N
    elif act == 'E':
        return E
    elif act == 'S':
        return S
    elif act == 'W':
        return W

def doAct(coord, d, num):
    if d == N:
        coord[1] += num
    elif d == E:
        coord[0] += num
    elif d == S:
        coord[1] -= num
    elif d == W:
        coord[0] -= num

def main():
    f = open("actions.txt")

    coord = [0, 0] # (x, y) coord
    curDir = E
    for line in f:
        act = line[0]
        num = int(line[1:].rstrip())
        if act == 'F':
            doAct(coord, curDir, num)
        elif act == 'R':
            curDir += (num // 90)
            curDir %= numDirs
        elif act == 'L':
            curDir -= (num // 90)
            curDir %= numDirs
        else:
            doAct(coord, actToDir(act), num)

    dist = 0
    for xi in coord:
        dist += abs(xi)
    print("Answer: " + str(dist))
    f.close()

if __name__ ==  "__main__":
    main()