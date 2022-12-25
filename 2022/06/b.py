import pprint

pp = pprint.PrettyPrinter()

def main():
    f = open("buffer.txt")

    line = f.readline().strip()
    for i in range(13, len(line)):
        if len(set(line[(i - 13):(i + 1)])) == 14:
            print(i + 1)
            break

if __name__ == "__main__":
    main()