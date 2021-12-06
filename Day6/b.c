#define _GNU_SOURCE
#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

const size_t days = 256;

void print_arr(size_t *arr, size_t len) {
    for (size_t i = 0; i < len; i++)
        printf("%zu ", arr[i]);
    printf("\n");
}

int main() {
    const char *file = "timers.txt";
    FILE *f = fopen(file, "r");
    char *line = NULL;
    size_t n = 0;

    size_t *ages = calloc(9, sizeof(size_t));

    getline(&line, &n, f);
    char *tok = strtok(line, ",");
    while (tok != NULL) {
        long num = strtol(tok, &tok, 10);
        ages[num]++;
        tok = strtok(NULL, ",");
    }

    for (size_t i = 0; i < days; i++) {
        print_arr(ages, 9);
        size_t *temp = calloc(9, sizeof(size_t));
        for (size_t age = 0; age < 9; age++)
            temp[age] = ages[(age + 1) % 9];
        temp[6] += ages[0];
        free(ages);
        ages = temp;
    }

    size_t ans = 0;
    for (size_t i = 0; i < 9; i++)
        ans += ages[i];

    printf("Answer: %zu\n", ans);
    free(ages);
    free(line);
    fclose(f);
    return 0;
}
