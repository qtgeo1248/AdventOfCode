import pprint

pp = pprint.PrettyPrinter()

def charToHex(c):
    hexVal = int(c, 16)
    bitArr = [0, 0, 0, 0]
    i = 3
    while hexVal > 0:
        bitArr[i] = hexVal % 2
        i = i - 1
        hexVal //= 2
    return bitArr

# lo is inclusive, hi is exclusive
def bitsToNum(bits, lo, hi):
    num = 0
    for i in range(lo, hi):
        num <<= 1
        num += bits[i]
    return num

# returns num bits processed
def processLiteral(bits, start):
    numBits = 0
    while bits[start] != 0:
        start += 5
        numBits += 5
    return numBits + 5

# lo is inclusive, hi is exclusive
# Returns (version sum, numProcessed)
def processBits(bits, lo):
    ver = bitsToNum(bits, lo, lo + 3)
    typeId = bitsToNum(bits, lo + 3, lo + 6)
    if typeId == 4:
        numProc = processLiteral(bits, lo + 6)
        return (ver, numProc + 6)
    else:
        typeId = bitsToNum(bits, lo + 6, lo + 7)
        numProc = 0
        if typeId: # equals 1
            numPackets = bitsToNum(bits, lo + 7, lo + 18)
            while numPackets > 0:
                (nextVer, nextProc) = processBits(bits, lo + 18 + numProc)
                numProc += nextProc
                ver += nextVer
                numPackets -= 1
            return (ver, numProc + 18)
        else:
            lenPackets = bitsToNum(bits, lo + 7, lo + 22)
            while numProc < lenPackets:
                (nextVer, nextProc) = processBits(bits, lo + 22 + numProc)
                numProc += nextProc
                ver += nextVer
            return (ver, numProc + 22)


def main():
    f = open("packet.txt")

    line = f.readline().rstrip()
    bits = []
    for c in line:
        bits.extend(charToHex(c))

    ans = processBits(bits, 0)

    print("Answer: " + str(ans[0]))
    f.close()

if __name__ ==  "__main__":
    main()