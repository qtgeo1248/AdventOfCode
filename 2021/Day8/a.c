#define _GNU_SOURCE
#include <assert.h>
#include <limits.h>
#include <stdint.h>
#include <stdbool.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

int main() {
    const char *file = "displays.txt";
    FILE *f = fopen(file, "r");
    char *line = NULL;
    size_t n = 0;

    size_t one = 0;
    size_t four = 0;
    size_t seven = 0;
    size_t eight = 0;

    while (getline(&line, &n, f) != EOF) {
        char *temp = strchr(line, '|');
        temp += 2;
        temp[strlen(temp) - 1] = '\0';
        char *tok = strtok(temp, " ");
        while (tok != NULL) {
            switch (strlen(tok)) {
                case 2:
                    one++;
                    break;
                case 4:
                    four++;
                    break;
                case 3:
                    seven++;
                    break;
                case 7:
                    eight++;
                    break;
            }
            tok = strtok(NULL, " ");
        }
    }

    printf("Answer: %zu\n", one + four + seven + eight);
    free(line);
    fclose(f);
    return 0;
}
