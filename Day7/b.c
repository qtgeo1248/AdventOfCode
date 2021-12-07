#define _GNU_SOURCE
#include <assert.h>
#include <stdint.h>
#include <stdbool.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

const size_t days = 80;

size_t myabs(long x) {
    return (size_t)(x >= 0 ? x : -1 * x);
}

void print_arr(long *arr, size_t len) {
    for (size_t i = 0; i < len; i++)
        printf("%ld ", arr[i]);
    printf("\n");
}

int main() {
    const char *file = "timers.txt";
    FILE *f = fopen(file, "r");
    char *line = NULL;
    size_t n = 0;

    size_t arr_len = 2;
    long *crabs = calloc(arr_len, sizeof(size_t));
    size_t num_read = 0;
    long max = 0;

    getline(&line, &n, f);
    char *tok = strtok(line, ",");
    while (tok != NULL) {
        long num = strtol(tok, &tok, 10);
        crabs[num_read] = num;
        num_read++;
        if (num_read >= arr_len) {
            crabs = realloc(crabs, 2 * arr_len * sizeof(size_t));
            arr_len *= 2;
        }
        if (num > max) max = num;
        tok = strtok(NULL, ",");
    }

    size_t total = SIZE_MAX;
    for (long i = 0; i <= max; i++) {
        size_t cur = 0;
        for (size_t j = 0; j < num_read; j++) {
            size_t dist = myabs(crabs[j] - i);
            cur += dist * (dist + 1) / 2;
        }
        if (cur < total)
            total = cur;
    }

    print_arr(crabs, num_read);

    printf("Answer: %zu\n", total);
    free(line);
    fclose(f);
    return 0;
}
