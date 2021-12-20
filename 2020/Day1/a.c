#include <stdlib.h>
#include <stdio.h>

size_t len_file(const char *filename) {
    FILE *f = fopen(filename, "r");
    size_t i = 0;
    while (!feof(f)) {
        int dummy = 0;
        fscanf(f, "%d", &dummy);
        i++;
    }
    fclose(f);
    return i;
}

int *get_ints(const char *filename, size_t len) {
    FILE *f = fopen(filename, "r");
    int *arr = calloc(sizeof(int), len);
    for (int i = 0; !feof(f); i++)
        fscanf(f, "%d", &arr[i]);
    fclose(f);
    return arr;
}

int main() {
    const char *file = "entries.txt";
    size_t n = len_file(file);
    int *arr = get_ints(file, n);

    long ans;

    for (size_t i = 0; i < n; i++)
        for (size_t j = i; j < n; j++)
            if (arr[i] + arr[j] == 2020)
                ans = arr[i] * arr[j];
    printf("Answer: %ld\n", ans);

    free(arr);

    return 0;
}