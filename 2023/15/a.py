import pprint

pp = pprint.PrettyPrinter(width=150)

# line = f.readline().rstrip()

def hash(s):
    cur = 0
    for c in s:
        cur = (17 * (cur + ord(c))) % 256
    return cur

def main():
    f = open("appendix.txt")

    line = f.readline().rstrip().split(",")
    pp.pprint(sum(map(hash, line)))

if __name__ == "__main__":
    main()
