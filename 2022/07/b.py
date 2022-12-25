import pprint

pp = pprint.PrettyPrinter()

class File:
    def __init__(self, name, size, parent, isFile):
        self.name = name
        self.size = size
        self.children = None if isFile else []
        self.parent = parent
        self.isFile = isFile

    def add(self, nextName, size, isFile):
        for child in self.children:
            if child.name == nextName:
                return child
        nex = File(nextName, size, self, isFile)
        self.children.append(nex)
        return nex

def findAns(file, brain):
    if file.isFile:
        return file.size
    else:
        totSum = 0
        for f in file.children:
            totSum += findAns(f, brain)
        brain[file] = totSum
        return totSum

def main():
    f = open("terminal.txt")

    cur = None
    top = File("/", None, None, False)

    for line in f:
        line = line.strip().split(" ")
        if line[0] == "$" and line[1] == "cd":
            if line[2] == "..":
                cur = cur.parent
            elif line[2] == "/":
                cur = top
            else:
                cur = cur.add(line[2], None, False)
        elif line[0] == "dir":
            cur.add(line[1], None, False)
        elif line[0] != "$":
            cur.add(line[1], int(line[0]), True)
    brain = dict()
    findAns(top, brain)

    dirs = list(brain.items())

    unused = 70000000 - brain[top]
    need = 30000000 - unused
    dirs.sort(key=lambda x: x[1])

    for (_, size) in dirs:
        if size >= need:
            print(size)
            break
            

if __name__ == "__main__":
    main()