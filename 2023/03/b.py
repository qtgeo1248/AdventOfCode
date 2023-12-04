from collections import defaultdict
import pprint

pp = pprint.PrettyPrinter(width=150)

# line = f.readline().rstrip()

dirs = {(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)}

def main():
    f = open("schematic.txt")
    gears = set()
    nums = defaultdict(lambda: set())
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
                    for coord in curCoords:
                        nums[coord].add((int(curNum), row, col))
                    curCoords = set()
                    curNum = ""
                if c == "*":
                    gears.add((row, col))
            col += 1
        row += 1
    ans = 0
    for coord in gears:
        if coord in nums and len(nums[coord]) == 2:
            prod = 1
            for num in nums[coord]:
                prod *= num[0]
            ans += prod
    print(ans)

if __name__ == "__main__":
    main()
