import pprint

pp = pprint.PrettyPrinter(width=150)

# line = f.readline().rstrip()

dirs = {(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)}

def main():
    f = open("schematic.txt")
    parts = set()
    nums = dict()
    row = 0
    for line in f:
        col = 0
        curCoords = set()
        curNum = ""
        for c in line:
            if c.isdigit():
                curNum += c
                for dir in dirs:
                    curCoords.add((row + dir[0], col + dir[1]))
            else:
                if curNum != "":
                    nums[(int(curNum), row, col)] = curCoords
                    curCoords = set()
                    curNum = ""
                if c != "." and c != "\n":
                    parts.add((row, col))
            col += 1
        row += 1
    ans = 0
    for (num, coords) in nums.items():
        if len(coords.intersection(parts)) > 0:
            ans += num[0]
    print(ans)

if __name__ == "__main__":
    main()
