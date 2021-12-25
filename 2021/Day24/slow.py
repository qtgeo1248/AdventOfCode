import pprint
import itertools 
from queue import PriorityQueue

pp = pprint.PrettyPrinter()
numDigits = 14

def idx(c):
    return ord('z') - ord(c)

def getVal(c, var):
    if c.isdigit() or c[1:].isdigit():
        return int(c)
    else:
        return var[idx(c)]

def model(inp, instr):
    var = [0, 0, 0, 0] # [z, y, x, w]
    for line in instr:
        if line[0] == 'inp':
            var[idx(line[1])] = inp.pop(0)
        elif line[0] == 'add':
            var[idx(line[1])] += getVal(line[2], var)
        elif line[0] == 'mul':
            var[idx(line[1])] *= getVal(line[2], var)
        elif line[0] == 'div':
            var[idx(line[1])] //= getVal(line[2], var)
        elif line[0] == 'mod':
            var[idx(line[1])] %= getVal(line[2], var)
        elif line[0] == 'eql':
            var[idx(line[1])] = int(var[idx(line[1])] == getVal(line[2], var))
    return var[0] == 0

def convert(inp):
    ans = 0
    for i in range(len(inp)):
        ans *= 10
        ans += inp[i]
    return ans

def main():
    f = open("instructions.txt")

    instr = []
    for line in f:
        instr.append(line.rstrip().split(" "))

    last = 0
    inputs = itertools.product([9, 8, 7, 6, 5, 4, 3, 2, 1], repeat=numDigits)
    for inp in inputs:
        if last != inp[8]:
            last = inp[8]
            print(convert(inp))
        if model(list(inp), instr):
            print("Answer: " + convert(inp))
            f.close()

    print("Answer: ")
    f.close()

if __name__ ==  "__main__":
    main()