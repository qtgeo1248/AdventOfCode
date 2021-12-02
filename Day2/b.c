#include <stdlib.h>
#include <stdio.h>
#include <string.h>

int main() {
    char *file = "commands.txt";
    FILE *f = fopen(file, "r");
    char *line = NULL;
    size_t n = 0;

    ssize_t depth = 0;
    ssize_t hor = 0;
    ssize_t aim = 0;

    while (getline(&line, &n, f) != -1) {
        char *num = strchr(line, ' ');
        num += 1;
        ssize_t integer = strtol(num, &num, 10);
        switch(line[0]) {
            case 'f': {
                hor += integer;
                depth += aim * integer;
                break;
            } case 'u': {
                aim -= integer;
                break;
            } case 'd': {
                aim += integer;
                break;
            }
        }
    }

    printf("Answer: %zd\n", depth * hor);
    
    return 0;
}
