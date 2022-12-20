import pprint

pp = pprint.PrettyPrinter()

key = 811589153

def move(id, idxs, mixer):
    n = id[0]
    if n == 0:
        return
    i = idxs[id]
    toMove = n % (len(mixer) - 1)
    for j in range(toMove):
        dest = (i + j) % len(mixer)
        mixer[dest] = mixer[(dest + 1) % len(mixer)]
        idxs[mixer[dest]] = dest
    mixer[(i + toMove) % len(mixer)] = id
    idxs[id] = (i + toMove) % len(mixer)

def main():
    f = open("file.txt")

    idxs = dict()
    og = []
    mixer = []
    zero = None
    for line in f:
        n = int(line.strip()) * key
        i = len(og)
        idxs[(n, i)] = i
        og.append((n, i))
        mixer.append((n, i))
        if n == 0:
            zero = (n, i)

    for _ in range(10):
        for (n, i) in og:
            move((n, i), idxs, mixer)

    ans = 0
    for i in range(1, 4):
        ans += mixer[(idxs[zero] + 1000 * i) % len(mixer)][0]
    print(ans)

if __name__ == "__main__":
    main()
