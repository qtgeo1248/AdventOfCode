from collections import defaultdict, deque
import pprint

pp = pprint.PrettyPrinter(width=150)

# line = f.readline().rstrip()

NUM_ITERS = 1000

class Module:
    def __init__(self, name, recvs, dests):
        self.name = name
        self.recvs = recvs
        self.dests = dests

    def pulse(self, recv, isHigh):
        return []
    
class Broadcast(Module):
    def pulse(self, recv, isHigh):
        return list(map(lambda dst: (self.name, isHigh, dst), self.dests))
    
    def __repr__(self):
        return "broadcaster"
    
class FlipFlop(Module):
    def __init__(self, name, recvs, dests):
        super().__init__(name, recvs, dests)
        self.power = False

    def pulse(self, recv, isHigh):
        if isHigh:
            return []
        self.power = not self.power
        return list(map(lambda dst: (self.name, self.power, dst), self.dests))
    
    def __repr__(self):
        return str((self.name, self.power))
    
class Conjunction(Module):
    def __init__(self, name, recvs, dests):
        super().__init__(name, recvs, dests)
        self.numHighs = 0
        self.memory = dict(map(lambda rec: (rec, False), self.recvs))

    def pulse(self, recv, isHigh):
        if self.memory[recv] != isHigh:
            self.memory[recv] = isHigh
            self.numHighs += 1 if isHigh else -1
        return list(map(lambda dst: (self.name, self.numHighs != len(self.recvs), dst), self.dests))

    def __repr__(self):
        return str((self.name, self.numHighs, self.memory))
    
def sendPulse(modules, numPulses):
    pulses = deque()
    pulses.append(("button", False, "broadcaster"))
    while len(pulses) > 0:
        (recv, isHigh, dst) = pulses.popleft()
        numPulses[1 if isHigh else 0] += 1
        pulses.extend(modules[dst].pulse(recv, isHigh))

def main():
    f = open("modules.txt")

    infos = dict()
    allModuleNames = set()
    receivers = defaultdict(lambda: set())
    for line in f:
        [first, dests] = line.rstrip().split(" -> ")
        dests = dests.split(", ")
        name, typ = None, None
        if first == "broadcaster":
            name = first
            typ = "b"
        elif first[0] == '%':
            name = first[1:]
            typ = "f"
        elif first[0] == '&':
            name = first[1:]
            typ = "c"
        else:
            name = first
            typ = "o"

        infos[name] = (typ, dests)
        for dst in dests:
            receivers[dst].add(name)
        allModuleNames.add(name)
        allModuleNames.update(set(dests))

    modules = dict()
    for name in allModuleNames:
        if name not in infos:
            modules[name] = Module(name, receivers[name], set())
        else:
            (typ, dsts) = infos[name]
            if typ == "b":
                modules[name] = Broadcast(name, receivers[name], dsts)
            elif typ == "f":
                modules[name] = FlipFlop(name, receivers[name], dsts)
            elif typ == "c":
                modules[name] = Conjunction(name, receivers[name], dsts)
            else:
                modules[name] = Module(name, receivers[name], dsts)
    numPulses = [0, 0]
    for _ in range(NUM_ITERS):
        sendPulse(modules, numPulses)
    pp.pprint(numPulses[0] * numPulses[1])

if __name__ == "__main__":
    main()
