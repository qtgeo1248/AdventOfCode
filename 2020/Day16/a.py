import pprint

pp = pprint.PrettyPrinter()

def valid(n, ranges):
    for r in ranges:
        if r[0] <= n <= r[1]:
            return True
    return False

def main():
    f = open("tickets.txt")
    ranges = []
    numNewLines = 0
    mine = None
    ans = 0
    for line in f:
        if line == "\n":
            numNewLines += 1
            f.readline()
        elif numNewLines == 0: # Rules
            rule = line.rstrip().split(": ")
            curRange = rule[1].split(" or ")
            for cur in curRange:
                cur = cur.split("-")
                ranges.append(tuple([int(c) for c in cur]))
        elif numNewLines == 1: # Your ticket
            mine = line.rstrip().split(",")
            mine = [int(n) for n in mine]
        else: # Nearby tickets
            nums = line.rstrip().split(",")
            nums = [int(n) for n in nums]
            for n in nums:
                if not valid(n, ranges):
                    ans += n
    print("Answer: " + str(ans))
    f.close()

if __name__ ==  "__main__":
    main()