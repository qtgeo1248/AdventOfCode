import math
import pprint

pp = pprint.PrettyPrinter(width=150)

# line = f.readline().rstrip()

def solns(t, d):
    descr = t * t - 4 * d
    if descr < 0:
        return None
    return ((t - math.sqrt(descr)) / 2, (t + math.sqrt(descr)) / 2)

def main():
    f = open("races.txt")
    timeLine = f.readline().rstrip()
    distanceLine = f.readline().rstrip()

    time = ""
    dist = ""

    for t in timeLine.split()[1:]:
        time += t
    for d in distanceLine.split()[1:]:
        dist += d

    soln = solns(int(time), int(dist))
    print(soln)
    if soln is not None:
        print(math.floor(soln[1] - 0.0000001) - math.ceil(soln[0] + 0.0000001) + 1)


if __name__ == "__main__":
    main()
