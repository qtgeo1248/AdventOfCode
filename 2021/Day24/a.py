import pprint
import itertools 
from queue import PriorityQueue

pp = pprint.PrettyPrinter()
numDigits = 14

def idx(c):
    return ord('z') - ord(c)

def model(inp, instr, brain):
    var = [0, 0, 0] # [z, y, x]
    i = 0
    numInstrPerInp = 18
    for digit in inp:
        # inp w
        # mul x 0
        # add x z
        # mod x 26
        var[idx('x')] = var[idx('z')] % 26
        # div z ___
        divz = int(instr[numInstrPerInp * i + 4][2])
        var[idx('z')] //= divz
        # add x ___
        addx = int(instr[numInstrPerInp * i + 5][2])
        var[idx('x')] += addx
        # eql x w
        # eql x 0
        var[idx('x')] = int(var[idx('x')] != digit)
        # mul y 0
        # add y 25
        # mul y x
        # add y 1
        var[idx('y')] = 25 * var[idx('x')] + 1
        # mul z y
        var[idx('z')] *= var[idx('y')]
        # mul y 0
        # add y w
        # add y ___
        # mul y x
        addy = int(instr[numInstrPerInp * i + 15][2])
        var[idx('y')] = (digit + addy) * var[idx('x')]
        # add z y
        var[idx('z')] += var[idx('y')]
        if i >= 5:
            if var[0] in brain:
                return False
            brain.add(var[0])
        i += 1
    return var[idx('z')] == 0

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

    brain = set() # Returns false states
    last = 0
    inputs = itertools.product([9, 8, 7, 6, 5, 4, 3, 2, 1], repeat=numDigits)
    for inp in inputs:
        if last != inp[9]:
            last = inp[9]
            print((convert(inp), len(brain)))
        if model(inp, instr, brain):
            print("Answer: " + str(convert(inp)))
            f.close()

    print("Answer: ")
    f.close()

if __name__ ==  "__main__":
    main()