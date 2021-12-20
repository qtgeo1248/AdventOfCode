#include <stdlib.h>
#include <stdio.h>

size_t len_file(const char *filename) {
    FILE *f = fopen(filename, "r");
    size_t i = 0;
    while (!feof(f)) {
        size_t dummy = 0;
        fscanf(f, "%zu", &dummy);
        i++;
    }
    fclose(f);
    return i;
}

size_t *get_ints(const char *filename, size_t len) {
    FILE *f = fopen(filename, "r");
    size_t *arr = calloc(sizeof(size_t), len);
    for (int i = 0; !feof(f); i++)
        fscanf(f, "%zu", &arr[i]);
    fclose(f);
    return arr;
}

int main() {
    const char *file = "entries.txt";
    size_t n = len_file(file);
    size_t *arr = get_ints(file, n);

    size_t ans = 0;

    for (size_t i = 0; i < n; i++)
        for (size_t j = i + 1; j < n; j++)
            for (size_t k = j + 1; k < n; k++)
                if (arr[i] + arr[j] + arr[k] == 2020)
                    ans = arr[i] * arr[j] * arr[k];
    printf("Answer: %ld\n", ans);

    free(arr);

    return 0;
}