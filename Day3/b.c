#include <assert.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <stdbool.h>

typedef struct thing {
    char *num;
    struct thing *next;
} number;

static number *delete(number *start, bool is_one, size_t i) {
    size_t num1 = 0;
    size_t num0 = 0;

    for (number *cur = start; cur != NULL; cur = cur->next) {
        if (cur->num[i] == '0') num0++;
        else num1++;
    }

    bool to_keep = (num1 < num0) ^ is_one;
    number *prev = NULL;
    number *cur = start;
    while (cur != NULL) {
        if (cur->num[i] - '0' != to_keep) {
            if (prev == NULL) start = cur->next;
            else prev->next = cur->next;
        } else
            prev = cur;
        cur = cur->next;
    }

    return start;   
}

static long get_final(const char *file, bool is_one) {
    FILE *f = fopen(file, "r");
    char *line = NULL;
    size_t n = 0;

    number *start = NULL;
    number *cur = start;

    while (getline(&line, &n, f) != -1) {
        size_t bit_len = strlen(line) - 1;
        number *to_add = calloc(1, sizeof(number));
        to_add->num = calloc(bit_len + 1, sizeof(char));
        strncpy(to_add->num, line, bit_len);

        if (start == NULL) {
            start = to_add;
            cur = start;
        } else {
            cur->next = to_add;
            cur = cur->next;
        }
    }

    char *final = NULL;
    size_t i = 0;
    while (final == NULL) {
        start = delete(start, is_one, i);
        if (start->next == NULL) final = start->num;
        i++;
    }

    fclose(f);
    return strtol(final, NULL, 2);
}

int main() {
    const char *file = "numbers.txt";

    long oxy_final = get_final(file, true);
    long co2_final = get_final(file, false);

    printf("Answer: %zu\n", oxy_final * co2_final);
    return 0;
}
