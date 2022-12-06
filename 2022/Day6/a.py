import pprint

pp = pprint.PrettyPrinter()

def main():
    f = open("buffer.txt")

    line = f.readline().strip()
    for i in range(3, len(line)):
        if len(set(line[(i - 3):(i + 1)])) == 4:
            print(i + 1)
            break

if __name__ == "__main__":
    main()