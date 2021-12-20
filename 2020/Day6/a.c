#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <stdbool.h>

size_t count_yes(bool *yes) {
    size_t count = 0;
    for (size_t i = 0; i < 26; i++)
        if (yes[i]) count++;
    return count;
}

int main() {
    const char *filename = "answers.txt";
    FILE *f = fopen(filename, "r");
    bool *yes = calloc(sizeof(bool), 26);
    char *person = NULL; size_t n = 0;
    size_t count = 0;

    while (getline(&person, &n, f) != -1) {
        if (strcmp(person, "\n") == 0) {
            count += count_yes(yes);
            free(yes);
            yes = calloc(sizeof(bool), 26);
        } else {
            for (size_t i = 0; i < strlen(person) - 1; i++)
                yes[person[i] - 'a'] = true;
        }
    }
    printf("Answer: %zu\n", count);
    free(person);
    fclose(f);
    return 0;
}