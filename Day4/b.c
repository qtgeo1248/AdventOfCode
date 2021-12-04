#define _GNU_SOURCE
#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

static const int len = 5;

typedef struct list {
    long *nums;
    struct list *next;
} node;

static void print_arr(long *nums) {
    for (size_t i = 0; i < len; i++) {
        for (size_t j = 0; j < len; j++)
            printf("%ld\t", nums[len * i + j]);
        printf("\n");
    }
    printf("\n");
}

static bool check(long *nums) {
    bool is_rows[5];
    for (size_t i = 0; i < 5; i++) is_rows[i] = true;
    for (size_t i = 0; i < 5; i++) {
        bool is_col = true;
        for (size_t j = 0; j < 5; j++) {
            if (nums[5 * i + j] != -1) { 
                is_col = false;
                is_rows[j] = false;
            }
        }
        if (is_col) return true;
    }
    for (size_t i = 0; i < 5; i++) 
        if (is_rows[i]) return true;
    return false;
}

static long compute(long *nums) {
    long ans = 0;
    for (size_t i = 0; i < len * len; i++)
        if (nums[i] != -1) ans += nums[i];
    return ans;
}

int main() {
    const char *file = "numbers.txt";
    FILE *f = fopen(file, "r");
    char *line = NULL;
    size_t n = 0;

    size_t num_called = 0;
    getline(&line, &n, f);
    long called[100];
    char *tok = strtok(line, ",");
    while (tok != NULL) {
        called[num_called] = strtol(tok, &tok, 10);
        num_called++;
        tok = strtok(NULL, ",");
    }

    node *start = NULL;
    node *cur = start;
    size_t cur_idx = 0;
    while (getline(&line, &n, f) != EOF) {
        if (line[0] == '\n') {
            node *new = calloc(1, sizeof(node));
            new->nums = calloc(len * len, sizeof(long));
            if (start == NULL) {
                start = new;
                cur = new;
            } else {
                cur->next = new;
                cur = cur->next;
            }
            cur_idx = 0;
        } else {
            char *temp = line;
            do {
                long num = strtol(temp, &temp, 10);
                cur->nums[cur_idx] = num;
                cur_idx++;
            } while (temp[0] != '\n');
        }
    }
    node *last = NULL;
    size_t i = 0;
    bool not_found = true;
    while (i < num_called && not_found) {
        node *prev = start;
        for (cur = start; cur != NULL; cur = cur->next) {
            for (size_t j = 0; j < len * len; j++)
                if (cur->nums[j] == called[i]) cur->nums[j] = -1;
            if (check(cur->nums)) {
                print_arr(cur->nums);
                last = cur;
                if (cur == start) { 
                    start = cur->next; 
                    prev = start;
                }
                else prev->next = cur->next;
            }
            if (start == NULL) not_found = false;
            prev = cur;
        }
        i++;
    }

    printf("Answer: %ld\n", compute(last->nums) * called[i - 1]);
    fclose(f);
    return 0;
}
