import pprint

pp = pprint.PrettyPrinter()

def main():
    f = open("assignments.txt")
    tot = 0
    for line in f:
        [e1, e2] = line.strip().split(",")
        e1 = [int(x) for x in e1.split("-")]
        e2 = [int(x) for x in e2.split("-")]
        if (e1[0] <= e2[0] and e2[1] <= e1[1]) or (e2[0] <= e1[0] and e1[1] <= e2[1]):
            tot += 1
    print(tot)

if __name__ == "__main__":
    main()