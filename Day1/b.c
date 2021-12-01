#include <stdlib.h>
#include <stdio.h>

size_t len_file(char *filename) {
    FILE *f = fopen(filename, "r");
    size_t i = 0;
    while (!feof(f)) {
        int dummy = 0;
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
    char *file = "Entries.txt";
    size_t n = len_file(file);
    size_t *arr = get_ints(file, n);
    size_t *sliding_sums = calloc(n, sizeof(size_t));

    size_t ans = 0;

    for (size_t i = 0; i < n; i++) {
        size_t start = (i / 4) * 4;
        if (i % 4 != 3)
            for (size_t offset = 0; offset < 4 && start + offset < n; offset++)
                sliding_sums[start + offset] += arr[i + offset];
    }

    for (size_t i = 1; i < n; i++)
        if (sliding_sums[i] > sliding_sums[i - 1])
            ans++;
        
    printf("Answer: %zu\n", ans);

    free(arr);
    free(sliding_sums);

    return 0;
}
