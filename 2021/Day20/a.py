import pprint
import math

pp = pprint.PrettyPrinter()
steps = 50
# (di, dj)
dirs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1)]

# Extend 2 units in each direction with blank dots, since they are affected by
# the og image
def extend(img, default):
    newImg = []
    newImg.append([default for _ in range(len(img[0]) + 2)])
    for line in img:
        newLine = [default]
        for c in line:
            newLine.append(c)
        newLine.append(default)
        newImg.append(newLine)
    newImg.append([default for _ in range(len(img[0]) + 2)])
    return newImg

def main():
    f = open("image.txt")

    algRaw = f.readline().rstrip()
    alg = [int(c == '#') for c in algRaw]
    f.readline()

    img = []
    for line in f:
        line = line.rstrip()
        img.append([int(c == '#') for c in line])
    # This is the "default" pixel for anything on the "outside"
    default = 0
    img = extend(img, default)
    
    for _ in range(steps):
        newImg = [[None for _ in range(len(img[0]))] for _ in range(len(img))]
        for i in range(len(img)):
            for j in range(len(img[0])):
                idx = 0
                for d in dirs:
                    (x, y) = (i + d[0], j + d[1])
                    idx <<= 1
                    if 0 <= x and x < len(img) and 0 <= y and y < len(img[0]):
                        idx += img[x][y]
                    else:
                        idx += default
                newImg[i][j] = alg[idx]
        default = alg[default * (len(alg) - 1)]
        img = extend(newImg, default)
        # if default = 0, newidx = 0; if default = 1, newidx = 2^9 - 1

    pixels = 0
    for i in range(len(img)):
        for j in range(len(img[0])):
            pixels += img[i][j]
    print("Answer: " + str(pixels))
    f.close()

if __name__ ==  "__main__":
    main()