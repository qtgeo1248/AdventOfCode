import pprint

pp = pprint.PrettyPrinter()

# Always points to a digit
def processSymbol(expr, sym, i):
    while True:
        if expr[i] == '(':
            process(expr, i + 1)
        elif i + 1 == len(expr):
            return
        elif expr[i + 1] == ')':
            if sym == '*': # You're only done with the parens if you are mult
                expr.pop(i + 1) # The ')' symbol
                expr.pop(i - 1) # The '(' symbol
            return
        else: # is a digit
            if expr[i + 2] == '(':
                process(expr, i + 3) # Basically removes parentheses
            if expr[i + 1] == sym:
                if sym == '+':
                    expr[i] = int(expr[i]) + int(expr[i + 2])
                if sym == '*':
                    expr[i] = int(expr[i]) * int(expr[i + 2])
                expr.pop(i + 1)
                expr.pop(i + 1)
            else:
                i += 2

def process(expr, i):
    processSymbol(expr, '+', i)
    processSymbol(expr, '*', i)

def main():
    f = open("homework.txt")
    ans = 0
    for line in f:
        expr = list(filter(lambda tok: tok != ' ', line.rstrip()))
        processSymbol(expr, '+', 0)
        processSymbol(expr, '*', 0)
        ans += expr[0]

    print("Answer: " + str(ans))
    f.close()

if __name__ ==  "__main__":
    main()