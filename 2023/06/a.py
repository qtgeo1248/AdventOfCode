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

    times = [int(time) for time in timeLine.split()[1:]]
    distances = [int(dist) for dist in distanceLine.split()[1:]]

    ans = 1
    for (time, dist) in zip(times, distances):
        soln = solns(time, dist)
        print(soln)
        if soln is not None:
            ans *= math.floor(soln[1] - 0.0000001) - math.ceil(soln[0] + 0.0000001) + 1
        
    print(ans)

if __name__ == "__main__":
    main()
