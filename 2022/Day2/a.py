import pprint

pp = pprint.PrettyPrinter()

# line = f.readline().rstrip()
points = {'X': 1, 'Y': 2, 'Z': 3, 'A': 1, 'B': 2, 'C': 3}

score = {(1, 1): 3, (2, 2): 3, (3, 3): 3, (1, 3): 0, (1, 2): 6, (2, 1): 0, (2, 3): 6, (3, 1): 6, (3, 2): 0}

def main():
    f = open("strat.txt")
    tot = 0
    for line in f:
        [A, B] = line.strip().split()
        tot += points[B] + score[(points[A], points[B])]
    print(tot)

if __name__ == "__main__":
    main()