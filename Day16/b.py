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

# returns (val, num bits processed)
def processLiteral(bits, start):
    numBits = 0
    val = 0
    while bits[start] != 0:
        val += bitsToNum(bits, start + 1, start + 5)
        val <<= 4
        start += 5
        numBits += 5
    val += bitsToNum(bits, start + 1, start + 5)
    return (val, numBits + 5)

# lo is inclusive, hi is exclusive
# Returns (value, numProcessed)
def processBits(bits, lo):
    typeId = bitsToNum(bits, lo + 3, lo + 6)
    if typeId == 4:
        (val, numProc) = processLiteral(bits, lo + 6)
        return (val, numProc + 6)
    else:
        val = None
        lenId = bitsToNum(bits, lo + 6, lo + 7)
        numProc = 0
        packets = []
        if lenId: # equals 1
            numPackets = bitsToNum(bits, lo + 7, lo + 18)
            offset = 18
            while numPackets > 0:
                (nextVal, nextProc) = processBits(bits, lo + 18 + numProc)
                numProc += nextProc
                numPackets -= 1
                packets.append(nextVal)
        else:
            lenPackets = bitsToNum(bits, lo + 7, lo + 22)
            offset = 22
            while numProc < lenPackets:
                (nextVal, nextProc) = processBits(bits, lo + 22 + numProc)
                numProc += nextProc
                packets.append(nextVal)
        if typeId == 0:
            val = 0
            for packet in packets:
                val += packet
        elif typeId == 1:
            val = 1
            for packet in packets:
                val *= packet
        elif typeId == 2:
            for packet in packets:
                val = packet if val is None or packet < val else val
        elif typeId == 3:
            for packet in packets:
                val = packet if val is None or packet > val else val
        elif typeId == 5:
            val = int(packets[0] > packets[1])
        elif typeId == 6:
            val = int(packets[0] < packets[1])
        elif typeId == 7:
            val = int(packets[0] == packets[1])
        return (val, numProc + offset)


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