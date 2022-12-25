#include <stdlib.h>
#include <stdio.h>

size_t len_file(char *filename) {
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

size_t *get_ints(char *filename, size_t len) {
    FILE *f = fopen(filename, "r");
    size_t *arr = calloc(sizeof(int), len);
    for (int i = 0; !feof(f); i++)
        fscanf(f, "%zu", &arr[i]);
    fclose(f);
    return arr;
}

int main() {
    char *file = "measurements.txt";
    size_t n = len_file(file);
    size_t *arr = get_ints(file, n);

    size_t ans = 0;

    for (size_t i = 1; i < n; i++)
        if (arr[i] > arr[i - 1])
            ans++;
    printf("Answer: %ld\n", ans);

    free(arr);

    return 0;
}
