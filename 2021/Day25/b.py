import pprint
import itertools 
from queue import PriorityQueue

pp = pprint.PrettyPrinter()
numDigits = 14
numInstrPerInp = 18

# numMults is how many times you multiplied by 26
# Returns None if no solution at this point in time, and the answer in string
# form otherwise
def model(z, inpIdx, numMults, numDivsLeft, instr):
    if inpIdx == numDigits:
        return '' if z == 0 else None
    for digit in range(9): # Tests digits 1 through 9
        digit += 1
        newZ = z
        newMults = numMults
        newDivs = numDivsLeft
        # inp w
        # mul x 0
        # add x z
        # mod x 26
        x = newZ % 26
        # div z ___
        divz = int(instr[numInstrPerInp * inpIdx + 4][2])
        newZ //= divz
        if divz == 26:
            newDivs -= 1
            newMults -= 1
        # add x ___
        addx = int(instr[numInstrPerInp * inpIdx + 5][2])
        x += addx
        # eql x w
        # eql x 0
        x = x != digit
        if x == 1:
            newMults += 1
            if newMults > newDivs: # No way for z to become 0
                continue
        # mul y 0
        # add y 25
        # mul y x
        # add y 1
        y = 25 * x + 1
        # mul z y
        newZ *= y
        # mul y 0
        # add y w
        # add y ___
        # mul y x
        addy = int(instr[numInstrPerInp * inpIdx + 15][2])
        y = (digit + addy) * x
        # add z y
        newZ += y

        # Edits values for next iteration of digits
        nextDigs = model(newZ, inpIdx + 1, newMults, newDivs, instr)
        if nextDigs is not None:
            return str(digit) + nextDigs
    return None

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

    numDivz = 0
    for i in range(numDigits):
        divz = int(instr[numInstrPerInp * i + 4][2])
        if divz == 26:
            numDivz += 1

    ans = model(0, 0, 0, numDivz, instr)
    print("Answer: " + ans)
    f.close()

if __name__ ==  "__main__":
    main()