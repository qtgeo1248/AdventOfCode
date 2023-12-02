import pprint

pp = pprint.PrettyPrinter()

# line = f.readline().rstrip()

def main():
    f = open("games.txt")
    games = 0
    colors = {"red": 12, "green": 13, "blue": 14}
    for line in f:
        [game, sets] = line.rstrip().split(": ")
        sets = sets.split("; ")
        gid = int(game.split(" ")[1])
        possible = True
        for ran in sets:
            ran = ran.split(", ")
            for pull in ran:
                [num, col] = pull.split(" ")
                if col not in colors or colors[col] < int(num):
                    possible = False
        if possible:
            games += gid
    print(games)

if __name__ == "__main__":
    main()
