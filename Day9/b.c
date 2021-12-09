#define _GNU_SOURCE
#include <assert.h>
#include <limits.h>
#include <stdint.h>
#include <stdbool.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

size_t get_ind(size_t i, size_t j, size_t w) {
    return i * w + j;
}

void print_heights(int *heights, size_t wid, size_t hei) {
    for (size_t i = 0; i < hei; i++) {
        for (size_t j = 0; j < wid; j++)
            printf("%d ", heights[get_ind(i, j, wid)]);
        printf("\n");
    }
}

void print_basins(size_t *basins, size_t wid, size_t hei) {
    for (size_t i = 0; i < hei; i++) {
        for (size_t j = 0; j < wid; j++)
            printf("%zu ", basins[get_ind(i, j, wid)]);
        printf("\n");
    }
}

void fill_basin(size_t i, size_t j, size_t wid, size_t hei, int *heights, size_t *basins, size_t id) {
    if (j == (size_t)(-1) || j >= wid || i == (size_t)(-1) || i >= hei
        || basins[get_ind(i, j, wid)] > 0 || heights[get_ind(i, j, wid)] == 9)
        return;
    basins[get_ind(i, j, wid)] = id;
    fill_basin(i, j - 1, wid, hei, heights, basins, id);
    fill_basin(i - 1, j, wid, hei, heights, basins, id);
    fill_basin(i, j + 1, wid, hei, heights, basins, id);
    fill_basin(i + 1, j, wid, hei, heights, basins, id);
}

int main() {
    const char *file = "heights.txt";
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
    size_t *basins = calloc(num_read, sizeof(size_t));
    size_t num_basins = 0;
    
    for (size_t i = 0; i < hei; i++) {
        for (size_t j = 0; j < wid; j++) {
            bool is_low = true;
            int h = heights[get_ind(i, j, wid)];
            if ((j > 0 && h >= heights[get_ind(i, j - 1, wid)])
                || (i > 0 && h >= heights[get_ind(i - 1, j, wid)])
                || (j < wid - 1 && h >= heights[get_ind(i, j + 1, wid)])
                || (i < hei - 1 && h >= heights[get_ind(i + 1, j, wid)]))
                is_low = false;
            if (is_low) {
                num_basins++;
                fill_basin(i, j, wid, hei, heights, basins, num_basins);
            }
        }
    }

    print_heights(heights, wid, hei);
    printf("\n");
    print_basins(basins, wid, hei);

    size_t *sizes = calloc(num_basins, sizeof(size_t));
    for (size_t i = 0; i < num_read; i++)
        if (basins[i] != 0)
            sizes[basins[i] - 1]++;
    
    size_t first = 0;
    size_t second = 0;
    size_t third = 0;
    for (size_t i = 0; i < num_basins; i++) {
        if (sizes[i] > first) {
            third = second;
            second = first;
            first = sizes[i];
        } else if (sizes[i] > second) {
            third = second;
            second = sizes[i];
        } else if (sizes[i] > third) {
            third = sizes[i];
        }
    }

    printf("Answer: %zu\n", first * second * third);
    free(heights);
    free(basins);
    free(sizes);
    free(line);
    fclose(f);
    return 0;
}
