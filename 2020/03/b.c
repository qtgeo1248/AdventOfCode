#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <stdbool.h>

size_t num_rows(const char *filename) {
    size_t n = 0;
    FILE *f = fopen(filename, "r");
    for (int c = fgetc(f); c != EOF; c = fgetc(f))
        if (c == '\n') n++;
    fclose(f);
    return n;
}

size_t num_cols(const char *filename) {
    size_t m = 0;
    FILE *f = fopen(filename, "r");
    for (int c = fgetc(f); c != '\n'; c = fgetc(f))
        m++;
    fclose(f);
    return m;
}

bool **get_trees(const char *filename, size_t n, size_t m) {
    FILE *f = fopen(filename, "r");
    bool **trees = calloc(sizeof(bool*), n);
    for (size_t i = 0; i < n; i++)
        trees[i] = calloc(sizeof(bool), m);
    
    int c;
    for (size_t i = 0; i < n; i++)
        for (size_t j = 0; j < m; j++) {
            c = fgetc(f);
            if (c == '\n') c = fgetc(f);
            if (c == '#') trees[i][j] = true;
        }

    fclose(f);
    return trees;
}

size_t encountered(bool **trees, size_t n, size_t m, size_t rowadd, size_t coladd) {
    size_t count = 0;
    size_t j = 0;
    for (size_t i = 0; i < n; i += rowadd) {
        if (trees[i][j]) count++;
        j = (j + coladd) % m;
    }

    return count;
}

int main() {
    const char *filename = "trees.txt";
    size_t n = num_rows(filename);
    size_t m = num_cols(filename);
    bool **trees = get_trees(filename, n, m);

    size_t count = 1;
    count *= encountered(trees, n, m, 1, 1);
    count *= encountered(trees, n, m, 1, 3);
    count *= encountered(trees, n, m, 1, 5);
    count *= encountered(trees, n, m, 1, 7);
    count *= encountered(trees, n, m, 2, 1);
    printf("Answer: %zu\n", count);

    for (size_t i = 0; i < n; i++)
        free(trees[i]);
    free(trees);
    
    return 0;
}