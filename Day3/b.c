#include <assert.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <stdbool.h>

typedef struct thing {
    char *num;
    struct thing *next;
} number;

number *delete(number *start, bool is_one, size_t i) {
    size_t num1 = 0;
    size_t num0 = 0;

    for (number *cur = start; cur != NULL; cur = cur->next) {
        if (cur->num[i] == '0') num0++;
        else num1++;
    }

    bool to_keep;
    if (num1 > num0) to_keep = is_one;
    else if (num1 < num0) to_keep = !is_one;
    else to_keep = is_one;

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

int main() {
    char *file = "numbers.txt";
    FILE *f = fopen(file, "r");
    char *line = NULL;
    size_t n = 0;
    size_t bit_len = 0;

    fclose(f);

    f = fopen(file, "r");
    number *oxy = NULL;
    number *co2 = NULL;
    number *oxy_cur = oxy;
    number *co2_cur = co2;

    while (getline(&line, &n, f) != -1) {
        bit_len = strlen(line) - 1;
        number *num_oxy = calloc(1, sizeof(number));
        number *num_co2 = calloc(1, sizeof(number));

        num_oxy->num = calloc(bit_len + 1, sizeof(char));
        strncpy(num_oxy->num, line, bit_len);
        num_co2->num = calloc(bit_len + 1, sizeof(char));
        strncpy(num_co2->num, line, bit_len);
        
        if (oxy == NULL) {
            oxy = num_oxy;
            co2 = num_co2;
            oxy_cur = oxy;
            co2_cur = co2;
        } else {
            oxy_cur->next = num_oxy;
            co2_cur->next = num_co2;

            oxy_cur = oxy_cur->next;
            co2_cur = co2_cur->next;
        }
    }

    char *oxy_final = NULL;
    char *co2_final = NULL;

    size_t i = 0;
    while (oxy_final == NULL || co2_final == NULL) {
        if (oxy_final == NULL) {
            oxy = delete(oxy, true, i);
            if (oxy->next == NULL) oxy_final = oxy->num;
        }
        if (co2_final == NULL) {
            co2 = delete(co2, false, i);
            if (co2->next == NULL) co2_final = co2->num;
        }
        i++;
    }
    printf("Answer: %zu\n", strtol(oxy_final, &oxy_final, 2) * strtol(co2_final, &co2_final, 2));
    fclose(f);
    return 0;
}
