#define _GNU_SOURCE
#include <assert.h>
#include <limits.h>
#include <stdint.h>
#include <stdbool.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

typedef struct list_header {
    char c;
    struct list_header *next;
} list;

typedef struct {
    list *head;
    list *tail;
} stack;

void print_list(stack *L) {
    for (list *cur = L->head; cur != L->tail; cur = cur->next)
        printf("%c ", cur->c);
    printf("\n");
}

int main() {
    const char *file = "chunks.txt";
    FILE *f = fopen(file, "r");
    char *line = NULL;
    size_t n = 0;

    size_t score = 0;

    while (getline(&line, &n, f) != EOF) {
        stack *chars = calloc(1, sizeof(stack));
        chars->head = calloc(1, sizeof(list));
        chars->tail = chars->head;

        bool no_err = true;
        for (size_t i = 0; line[i] != '\n' && no_err; i++) {
            char c = line[i];
            if (c == '(' || c == '{' || c == '[' || c == '<') {
                list *append = calloc(1, sizeof(list));
                append->c = c;
                append->next = chars->head;
                chars->head = append;
            } else {
                char top = chars->head->c;
                if ((c == ')' && top != '(') || (c == '}' && top != '{')
                    || (c == '>' && top != '<') || (c == ']' && top != '[')) {
                    if (c == ')') score += 3;
                    if (c == ']') score += 57;
                    if (c == '}') score += 1197;
                    if (c == '>') score += 25137;
                    no_err = false;
                } else {
                    list *to_free = chars->head;
                    chars->head = chars->head->next;
                    free(to_free);
                }
            }
        }
    }

    printf("Answer: %zu\n", score);
    free(line);
    fclose(f);
    return 0;
}
