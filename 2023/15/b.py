import pprint

pp = pprint.PrettyPrinter(width=150)

# line = f.readline().rstrip()

class Box:
    def __init__(self):
        self.slots = []
        self.labelToSlot = dict()

    def remove(self, label):
        if label in self.labelToSlot:
            self.slots[self.labelToSlot[label]] = None
            del self.labelToSlot[label]

    def add(self, label, focalLen):
        if label in self.labelToSlot:
            self.slots[self.labelToSlot[label]] = focalLen
        else:
            self.labelToSlot[label] = len(self.slots)
            self.slots.append(focalLen)

    def __repr__(self):
        return str((self.slots, self.labelToSlot))
    
class Boxes:
    def __init__(self):
        self.boxes = [Box() for _ in range(256)]

    def remove(self, label):
        self.boxes[hash(label)].remove(label)

    def add(self, label, focalLen):
        self.boxes[hash(label)].add(label, focalLen)

    def power(self):
        tot = 0
        for i in range(len(self.boxes)):
            slotNum = 1
            for foc in self.boxes[i].slots:
                if foc is not None:
                    tot += (i + 1) * slotNum * foc
                    slotNum += 1
        return tot

    def __repr__(self):
        return str(list(filter(lambda box: len(box[1].labelToSlot) > 0, enumerate(self.boxes))))

def hash(s):
    cur = 0
    for c in s:
        cur = (17 * (cur + ord(c))) % 256
    return cur

def main():
    f = open("appendix.txt")
    line = f.readline().rstrip().split(",")
    boxes = Boxes()
    for instr in line:
        if instr[-1] == '-':
            label = instr[:-1]
            boxes.remove(label)
        else:
            [label, focalLen] = instr.split("=")
            boxes.add(label, int(focalLen))
    pp.pprint(boxes.power())

if __name__ == "__main__":
    main()
