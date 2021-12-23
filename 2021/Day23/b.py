import pprint
from queue import PriorityQueue

pp = pprint.PrettyPrinter()
HALL = 1
ROOM = 0
WALL = -1
numFrogsPerRoom = 4

def cost(steps, typeFrog):
    return steps * (10 ** (ord(typeFrog) - ord('A')))

def getDest(typeFrog):
    return 2 * (ord(typeFrog) - ord('A')) + 3

def done(frogStates):
    for (coords, _, typeFrog) in frogStates:
        if coords[1] != getDest(typeFrog):
            return False
    return True

def blockedInRoom(x, y, takenCoords):
    for i in range(numFrogsPerRoom - 1):
        if (x - i - 1, y) in takenCoords:
            return True
    return False

# Gives possible y coords in the hall
def possNextHallway(board, hallx, y, takenCoords):
    poss = []
    goRight = True
    goLeft = True
    for d in range(1, len(board[hallx])):
        if (hallx, y + d) in takenCoords:
            goRight = False
        if (hallx, y - d) in takenCoords:
            goLeft = False
        if goRight and y + d < len(board[hallx]) and board[hallx][y + d] == HALL and board[hallx + 1][y + d] != ROOM:
            poss.append(y + d)
        if goLeft and 0 <= y - d and board[hallx][y - d] == HALL and board[hallx + 1][y - d] != ROOM:
            poss.append(y - d)
    return poss

# gives possible (x, y) coords in the room next
def possNextRoom(board, hallx, y, takenCoords, typeFrog):
    poss = []
    goRight = True
    goLeft = True
    for d in range(1, len(board[hallx])):
        if (hallx, y + d) in takenCoords:
            goRight = False
        if (hallx, y - d) in takenCoords:
            goLeft = False
        if goRight and y + d == getDest(typeFrog):
            poss.append(y + d)
        if goLeft and y - d == getDest(typeFrog):
            poss.append(y - d)
    newPoss = []
    for newY in poss:
        deepest = 0
        deepness = 1
        while deepness <= numFrogsPerRoom:
            if (hallx + deepness, newY) not in takenCoords:
                deepest = deepness
            deepness += 1
        if deepest > 0:
            newPoss.append((hallx + deepest, newY))
    return newPoss

# Gives an array of new states possible, in the format for a priority queue
def getNextSteps(board, hallx, c, state):
    takenCoords = set()
    for s in state:
        takenCoords.add(s[0])
    otherFrogs = set(state)
    nextStates = []
    for i in range(len(state)):
        if not state[i][1]:
            takenCoords.remove(state[i][0])
            otherFrogs.remove(state[i])
            (x, y) = state[i][0]
            possLocs = None
            if board[x][y] == ROOM and not blockedInRoom(x, y, takenCoords):
                possLocs = possNextHallway(board, hallx, y, takenCoords)
            if board[x][y] == HALL:
                possLocs = possNextRoom(board, hallx, y, takenCoords, state[i][2])
            if possLocs is not None:
                for poss in possLocs:
                    newC = cost(abs(x - poss[0]) + abs(y - poss[1]) if board[x][y] == HALL else x - hallx + abs(y - poss), state[i][2])
                    newPoss = poss if board[x][y] == HALL else (hallx, poss)
                    newState = list(otherFrogs)
                    newState.append((newPoss, True if board[x][y] == HALL else state[i][1], state[i][2]))
                    nextStates.append((c + newC, tuple(newState)))
            takenCoords.add(state[i][0])
            otherFrogs.add(state[i])
    return nextStates

def minCost(board, hallx, initFrogs):
    # Stores (cost, frogStates)
    # frogStates are a bunch of tuples of ((x, y), isDoneMoving, Type)
    paths = PriorityQueue()
    paths.put((0, tuple(initFrogs)))
    costs = {} # memoization
    while not paths.empty():
        (cost, state) = paths.get()
        if done(state):
            return cost
        nextStates = getNextSteps(board, hallx, cost, state)
        for nextState in nextStates:
            frogs = list(nextState[1])
            frogs.sort(key = lambda x: (x[2], x[1], x[0]))
            frogs = tuple(frogs)
            if frogs not in costs.keys() or nextState[0] < costs[frogs]:
                paths.put(nextState)
                costs[frogs] = nextState[0]
    return None

def main():
    f = open("burrow.txt")

    board = [] # each element is either HALL, ROOM, or WALL
    initFrogs = [] # Tuples of frog states: ((x, y), isDoneMoving, Type)
    # Note x goes vertically and y goes horizontally
    x = 0
    hallx = None
    for line in f:
        line = line.rstrip()
        row = []
        isRoom = False
        for y in range(len(line)):
            c = line[y]
            if ord('A') <= ord(c) <= ord('Z'):
                isRoom = True
                row.append(ROOM)
                initFrogs.append(((x if x == hallx + 1 else x + 2, y), False, c))
            elif c == '.':
                hallx = x
                row.append(HALL)
            else:
                row.append(WALL)
        if isRoom:
            board.append(row) # Need to append twice
        board.append(row)
        x += 1
    newFrogs = [((3, 3), False, 'D'), ((3, 5), False, 'C'), ((3, 7), False, 'B'), ((3, 9), False, 'A'),
                ((4, 3), False, 'D'), ((4, 5), False, 'B'), ((4, 7), False, 'A'), ((4, 9), False, 'C')]
    for frog in newFrogs:
        initFrogs.append(frog)

    print("Answer: " + str(minCost(board, hallx, initFrogs)))
    f.close()

if __name__ ==  "__main__":
    main()