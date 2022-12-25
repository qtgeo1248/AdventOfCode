import pprint

pp = pprint.PrettyPrinter()

snafuToDec = {"=": -2, "-": -1, "0": 0, "1": 1, "2": 2}
decToSnafu = {0: "0", 1: "1", 2: "2", -1: "-", -2: "="}

def toDec(snafu):
    ans = 0
    for c in snafu:
        ans = ans * 5 + snafuToDec[c]
    return ans

def toSnafu(dec):
    if dec == 0:
        return ""
    elif dec % 5 <= 2:
        return toSnafu(dec // 5) + decToSnafu[dec % 5]
    else:
        return toSnafu(dec // 5 + 1) + decToSnafu[dec % 5 - 5]

def main():
    f = open("fuel.txt")

    tot = 0

    for line in f:
        tot += toDec(line.strip())
    print(toSnafu(tot))

if __name__ == "__main__":
    main()
