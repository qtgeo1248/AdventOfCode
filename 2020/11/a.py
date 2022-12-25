import pprint

pp = pprint.PrettyPrinter()
dirs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
FLO = -1
EMP = 0
OCC = 1
tolerance = 4

def main():
    f = open("ferry.txt")
    # 1 = seat, 0 = empty, -1 = floor
    seats = []
    for line in f:
        line = line.rstrip()
        seats.append([(OCC if c == '#' else EMP if c == 'L' else FLO) for c in line])
    
    didChange = True
    while didChange:
        newSeats = [[None for _ in range(len(seats[i]))] for i in range(len(seats))]
        didChange = False
        for i in range(len(seats)):
            for j in range(len(seats[i])):
                count = 0
                for d in dirs:
                    if 0 <= i + d[0] < len(seats) and 0 <= j + d[1] < len(seats[i]) and seats[i + d[0]][j + d[1]] == OCC:
                        count += 1
                if seats[i][j] == EMP and count == 0:
                    newSeats[i][j] = OCC
                    didChange = True
                elif seats[i][j] == OCC and count >= tolerance:
                    newSeats[i][j] = EMP
                    didChange = True
                else:
                    newSeats[i][j] = seats[i][j]
        seats = newSeats

    numOcc = 0
    for i in range(len(seats)):
        for j in range(len(seats[i])):
            if seats[i][j] == OCC:
                numOcc += 1
    print("Answer: " + str(numOcc))
    f.close()

if __name__ ==  "__main__":
    main()