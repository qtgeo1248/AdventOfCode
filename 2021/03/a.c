#include <stdbool.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

int main() {
    const char *file = "numbers.txt";
    FILE *f = fopen(file, "r");
    char *line = NULL;
    size_t n = 0;
    size_t bit_len = 0;
    size_t *counts_one = NULL;
    size_t num_read = 0;


    while (getline(&line, &n, f) != EOF) {
        if (counts_one == NULL) { 
            bit_len = strlen(line) - 1;
            counts_one = calloc(bit_len, sizeof(size_t));
        }
        for (size_t i = 0; i < bit_len; i++)
            counts_one[i] += (size_t)(line[i] - '0');
        num_read++;
    }

    size_t gamma = 0;
    size_t epsilon = 0;
    for (size_t i = 0; i < bit_len; i++) {
        bool is_one = counts_one[i] >= num_read / 2;
        gamma = (gamma << 1) + (size_t)(is_one);
        epsilon = (epsilon << 1) + (size_t)(!is_one);
    }

    printf("Answer: %zu\n", gamma * epsilon);
    fclose(f);
    return 0;
}
