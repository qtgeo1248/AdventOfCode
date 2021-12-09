#define _GNU_SOURCE
#include <assert.h>
#include <limits.h>
#include <stdint.h>
#include <stdbool.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

void print_arr(int *heights, size_t wid, size_t hei) {
    for (size_t i = 0; i < hei; i++) {
        for (size_t j = 0; j < wid; j++)
            printf("%d ", heights[wid * i + j]);
        printf("\n");
    }
}

size_t get_ind(size_t i, size_t j, size_t w) {
    return i * w + j;
}

int main() {
    const char *file = "positions.txt";
    FILE *f = fopen(file, "r");
    char *line = NULL;
    size_t n = 0;

    size_t wid = 0;
    size_t num_read = 0;
    size_t len = 2;
    int *heights = calloc(len, sizeof(int));

    while (getline(&line, &n, f) != EOF) {
        for (size_t i = 0; line[i] != '\n'; i++) {
            heights[num_read] = line[i] - '0';
            num_read++;
            if (num_read >= len) {
                len *= 2;
                heights = realloc(heights, len * sizeof(int));
            }
        }
        wid = strlen(line) - 1;
    }

    size_t hei = num_read / wid;
    
    size_t risk = 0;
    for (size_t i = 0; i < hei; i++) {
        for (size_t j = 0; j < wid; j++) {
            bool is_low = true;
            int h = heights[get_ind(i, j, wid)];
            if (j > 0 && h >= heights[get_ind(i, j - 1, wid)]) is_low = false;
            if (i > 0 && h >= heights[get_ind(i - 1, j, wid)]) is_low = false;
            if (j < wid - 1 && h >= heights[get_ind(i, j + 1, wid)]) is_low = false;
            if (i < hei - 1 && h >= heights[get_ind(i + 1, j, wid)]) is_low = false;
            if (is_low) risk += (unsigned int)(h + 1);
        }
    }


    printf("Answer: %zu\n", risk);
    free(heights);
    free(line);
    fclose(f);
    return 0;
}
