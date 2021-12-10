#define _GNU_SOURCE
#include <assert.h>
#include <limits.h>
#include <stdint.h>
#include <stdbool.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

typedef struct c_list_header {
    char c;
    struct c_list_header *next;
} c_list;

typedef struct s_list_header {
    size_t s;
    struct s_list_header *next;
} s_list;

typedef struct {
    c_list *head;
    c_list *tail;
} c_stack;

typedef struct {
    s_list *head;
    s_list *tail;
} s_stack;

void print_slist(s_stack *L) {
    for (s_list *cur = L->head; cur != L->tail; cur = cur->next)
        printf("%zu ", cur->s);
    printf("\n");
}

void print_clist(c_stack *L) {
    for (c_list *cur = L->head; cur != L->tail; cur = cur->next)
        printf("%c ", cur->c);
    printf("\n");
}

int main() {
    const char *file = "chunks.txt";
    FILE *f = fopen(file, "r");
    char *line = NULL;
    size_t n = 0;

    s_stack *scores = calloc(1, sizeof(s_stack));
    scores->head = calloc(1, sizeof(s_list));
    scores->tail = scores->head;
    size_t num_wrong = 0;

    while (getline(&line, &n, f) != EOF) {
        c_stack *chars = calloc(1, sizeof(c_stack));
        chars->head = calloc(1, sizeof(c_list));
        chars->tail = chars->head;

        bool no_err = true;
        for (size_t i = 0; line[i] != '\n' && no_err; i++) {
            char c = line[i];
            if (c == '(' || c == '{' || c == '[' || c == '<') {
                c_list *append = calloc(1, sizeof(c_list));
                append->c = c;
                append->next = chars->head;
                chars->head = append;
            } else {
                char top = chars->head->c;
                if ((c == ')' && top != '(') || (c == '}' && top != '{')
                    || (c == '>' && top != '<') || (c == ']' && top != '[')) {
                    no_err = false;
                } else {
                    c_list *to_free = chars->head;
                    chars->head = chars->head->next;
                    free(to_free);
                }
            }
        }
        if (no_err) {
            num_wrong++;
            size_t score = 0;
            for (c_list *cur = chars->head; cur != chars->tail; cur = cur->next) {
                score *= 5;
                char c = cur->c;
                if (c == '(') score += 1;
                if (c == '[') score += 2;
                if (c == '{') score += 3;
                if (c == '<') score += 4;
            }
            s_list *new = calloc(1, sizeof(s_list));
            new->s = score;
            bool not_found = true;
            s_list *cur = scores->head;
            s_list *prev = NULL;
            while (cur != scores->tail && not_found) {
                if (score < cur->s) {
                    if (prev == NULL) {
                        new->next = scores->head;
                        scores->head = new;
                    } else {
                        prev->next = new;
                        new->next = cur;
                    }
                    not_found = false;
                } else {
                    prev = cur;
                    cur = cur->next;
                }
            }
            if (not_found) {
                scores->tail->s = score;
                scores->tail->next = new;
                scores->tail = new;
            }
        }
    }

    s_list *cur = scores->head;
    for (size_t i = 0; i < num_wrong / 2; i++)
        cur = cur->next;
    printf("Answer: %zu\n", cur->s);
    free(line);
    fclose(f);
    return 0;
}
