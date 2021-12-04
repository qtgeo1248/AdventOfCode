#define _GNU_SOURCE
#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

typedef struct list {
    long *nums;
    struct list *next;
} node;

static void print_arr(long *nums) {
    for (size_t i = 0; i < 5; i++) {
        for (size_t j = 0; j < 5; j++)
            printf("%ld\t", nums[5 * i + j]);
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
    // bool is_diag = true;
    // bool is_diag_other = true;
    for (size_t i = 0; i < 5; i++) { 
        if (is_rows[i]) return true;
    //     if (nums[5 * i + i] != -1) is_diag = false;
    //     if (nums[5 * i + 4 - i] != -1) is_diag_other = false;
    }
    // if (is_diag || is_diag_other) return true;
    return false;
}

static long compute(long *nums) {
    long ans = 0;
    for (size_t i = 0; i < 25; i++) {
        if (nums[i] != -1) ans += nums[i];
    }
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
            new->nums = calloc(25, sizeof(long));
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
    long ans = 0;
    size_t i = 0;
    bool not_found = true;
    for (; i < num_called && not_found; i++) {
        for (cur = start; cur != NULL && not_found; cur = cur->next) {
            for (size_t j = 0; j < 25; j++) {
                if (cur->nums[j] == called[i])
                    cur->nums[j] = -1;
            }
            if (check(cur->nums)) {
                print_arr(cur->nums);
                ans = compute(cur->nums);
                not_found = false;
            }
        }
    }

    printf("Answer: %ld\n", ans * called[i - 1]);
    fclose(f);
    return 0;
}
