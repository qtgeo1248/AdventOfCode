#include <stdlib.h>
#include <stdio.h>

size_t len_file(char *filename) {
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

int *get_ints(char *filename, size_t len) {
    FILE *f = fopen(filename, "r");
    int *arr = calloc(sizeof(int), len);
    for (int i = 0; !feof(f); i++)
        fscanf(f, "%d", &arr[i]);
    fclose(f);
    return arr;
}

int main() {
    char *file = "Entries.txt";
    int n = len_file(file);
    int *arr = get_ints(file, n);

    size_t ans = 0;

    for (int i = 1; i < n; i++)
        if (arr[i] > arr[i - 1])
            ans++;
    printf("Answer: %ld\n", ans);

    free(arr);

    return 0;
}