import pprint

pp = pprint.PrettyPrinter()

def main():
    f = open("program.txt")

    cycle = 0
    sprite = 1
    picture = []

    for line in f:
        line = line.strip().split()
        picture.append("#" if abs(cycle % 40 - sprite) <= 1 else ".")
        cycle += 1
        if cycle > 240:
            break
        if line[0] == "addx":
            picture.append("#" if abs(cycle % 40 - sprite) <= 1 else ".")
            sprite += int(line[1])
            cycle += 1
            if cycle > 240:
                break
    for i in range(6):
        print("".join(picture[(40 * i):(40 * (i + 1))]))

if __name__ == "__main__":
    main()