from collections import defaultdict
import pprint

pp = pprint.PrettyPrinter()

# line = f.readline().rstrip()

def main():
    f = open("games.txt")
    powers = 0
    for line in f:
        [_, sets] = line.rstrip().split(": ")
        colors = defaultdict(lambda: 0)
        sets = sets.split("; ")
        for ran in sets:
            ran = ran.split(", ")
            for pull in ran:
                [num, col] = pull.split(" ")
                colors[col] = max(colors[col], int(num))
        power = 1
        for count in colors.values():
            power *= count
        powers += power
    print(powers)

if __name__ == "__main__":
    main()
