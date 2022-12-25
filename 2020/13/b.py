import pprint
import math

pp = pprint.PrettyPrinter()

def main():
    f = open("notes.txt")

    leave = int(f.readline().rstrip())
    busses = f.readline().rstrip().split(",")

    curTime = 0
    curMult = 1
    numBus = 0
    for bus in busses:
        if bus.isdigit():
            bus = int(bus)
            while (curTime % bus) != (bus - numBus) % bus:
                curTime += curMult
            curMult = math.lcm(curMult, bus)
        numBus += 1

    print("Answer: " + str(curTime))
    f.close()

if __name__ ==  "__main__":
    main()