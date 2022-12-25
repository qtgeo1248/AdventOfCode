import pprint

pp = pprint.PrettyPrinter()

def main():
    f = open("notes.txt")

    leave = int(f.readline().rstrip())
    busses = f.readline().rstrip().split(",")

    minWait = None
    minId = None
    for bus in busses:
        if bus.isdigit():
            bus = int(bus)
            wait = bus - (leave % bus)
            if minWait is None or wait < minWait:
                minWait = wait
                minId = bus

    print("Answer: " + str(minId * minWait))
    f.close()

if __name__ ==  "__main__":
    main()