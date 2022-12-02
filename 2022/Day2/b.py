import pprint

pp = pprint.PrettyPrinter()

# line = f.readline().rstrip()
points = {'X': 0, 'Y': 3, 'Z': 6, 'A': 1, 'B': 2, 'C': 3}

score = {(1, 0): 3, (1, 3): 1, (1, 6): 2, (2, 0): 1, (2, 3): 2, (2, 6): 3, (3, 0): 2, (3, 3): 3, (3, 6): 1}

def main():
    f = open("strat.txt")
    tot = 0
    for line in f:
        [A, B] = line.strip().split()
        tot += points[B] + score[(points[A], points[B])]
    print(tot)

if __name__ == "__main__":
    main()