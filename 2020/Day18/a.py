import pprint

pp = pprint.PrettyPrinter()

# Edits expr so the only element left is the answer
# i must always point to a digit or a '('
def process(expr, i):
    while True:
        if expr[i] == '(':
            process(expr, i + 1)
        elif i + 1 == len(expr):
            return
        elif expr[i + 1] == ')':
            expr.pop(i + 1) # The ')' symbol
            expr.pop(i - 1) # The '(' symbol
            return
        else: # is a digit
            if expr[i + 2] == '(':
                process(expr, i + 3) # Basically removes parentheses
            if expr[i + 1] == '+':
                expr[i] = int(expr[i]) + int(expr[i + 2])
            elif expr[i + 1] == '*':
                expr[i] = int(expr[i]) * int(expr[i + 2])
            expr.pop(i + 1)
            expr.pop(i + 1)

def main():
    f = open("homework.txt")
    ans = 0
    for line in f:
        expr = list(filter(lambda tok: tok != ' ', line.rstrip()))
        process(expr, 0)
        ans += expr[0]

    print("Answer: " + str(ans))
    f.close()

if __name__ ==  "__main__":
    main()