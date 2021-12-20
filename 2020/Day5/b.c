#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <stdbool.h>

size_t find_empty(bool *seats) {
    for (size_t i = 8; i < 126 * 8 + 7; i++)
        if (seats[i - 1] && !seats[i] && seats[i + 1]) return i;
    return 0;
}

int main() {
    const char *filename = "seats.txt";
    FILE *f = fopen(filename, "r");
    bool *seats = calloc(sizeof(bool), 128 * 8);
    char *seat = NULL; size_t n = 0;

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
        seats[id] = true;
    }
    printf("Answer: %zu\n", find_empty(seats));
    free(seat);
    free(seats);
    fclose(f);
    return 0;
}