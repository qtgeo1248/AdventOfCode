#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <stdbool.h>

int main() {
    const char *filename = "seats.txt";
    FILE *f = fopen(filename, "r");
    char *seat = NULL;
    size_t n = 0;
    size_t max = 0;

    while (getline(&seat, &n, f) != -1) {
        size_t low = 0; size_t high = 127;
        for (int i = 0; i < 7; i++) {
            if (seat[i] == 'F') high -= (high - low + 1) / 2;
            else low += (high - low + 1) / 2;
        }
        size_t row = low;
        low = 0; high = 7;
        for (int i = 7; i < 10; i++) {
            if (seat[i] == 'L') high -= (high - low + 1) / 2;
            else low += (high - low + 1) / 2;
        }
        size_t col = low;
        size_t id = row * 8 + col;
        if (id > max) max = id;
    }
    printf("Answer: %zu\n", max);
    free(seat);
    fclose(f);
    return 0;
}