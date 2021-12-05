#define _GNU_SOURCE
#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

typedef struct list {
    long x1;
    long y1;
    long x2;
    long y2;
    struct list *next;
} node;

static long absv(long x) {
    return x >= 0 ? x : -1 * x;
}

static long incr(long x2, long x1) {
    if (x1 == x2) return 0;
    else return (x2 - x1) / absv(x2 - x1);
}

static void print_grid(long *grid, long wid, long height) {
    for (long i = 0; i < height; i++) {
        for (long j = 0; j < wid; j++)
            printf("%ld ", grid[wid * i + j]);
        printf("\n");
    }
}

int main() {
    const char *file = "numbers.txt";
    FILE *f = fopen(file, "r");
    char *line = NULL;
    size_t n = 0;

    long max_x = 0;
    long max_y = 0;

    node *start = calloc(1, sizeof(node));
    node *end = start;

    while (getline(&line, &n, f) != EOF) {
        char *temp = line;
        long x1 = strtol(temp, &temp, 10);
        long y1 = strtol(temp + 1, &temp, 10);
        long x2 = strtol(strchr(temp, '>') + 2, &temp, 10);
        long y2 = strtol(temp + 1, &temp, 10);
        if (x1 == x2 || y1 == y2) {
            if (x1 > max_x) max_x = x1;
            if (x2 > max_x) max_x = x2;
            if (y1 > max_y) max_y = y1;
            if (y2 > max_y) max_y = y2;
            end->x1 = x1;
            end->x2 = x2;
            end->y1 = y1;
            end->y2 = y2;
            end->next = calloc(1, sizeof(node));
            end = end->next;
        }
    }

    max_x++;
    max_y++;
    long *grid = calloc((size_t)(max_x * max_y), sizeof(size_t));
    for (node *cur = start; cur != end; cur = cur->next) {
        long x = cur->x1;
        long y = cur->y1;
        long dx = incr(cur->x2, cur->x1);
        long dy = incr(cur->y2, cur->y1);
        while ((x != cur->x2 + dx) || (y != cur->y2 + dy)) {
            printf("(%ld, %ld) ", x, y);
            (grid[max_x * y + x])++;
            x += dx;
            y += dy;
        }
        printf("\n");
    }

    print_grid(grid, max_x, max_y);

    size_t ans = 0;
    for (size_t i = 0; i < (size_t)(max_x * max_y); i++)
        if (grid[i] > 1)
            ans++;

    printf("Answer: %zu\n", ans);
    fclose(f);
    return 0;
}
