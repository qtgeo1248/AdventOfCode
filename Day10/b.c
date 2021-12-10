#define _GNU_SOURCE
#include <assert.h>
#include <limits.h>
#include <stdint.h>
#include <stdbool.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

typedef struct list_header {
    union {
        char ch;
        size_t sc;
    };
    struct list_header *next;
} list;

typedef struct {
    list *head;
    list *tail;
} stack;

void print_slist(stack *L, bool is_char) {
    for (list *cur = L->head; cur != L->tail; cur = cur->next) {
        if (is_char) printf("%c ", cur->ch);
        else printf("%zu ", cur->sc);
    }
    printf("\n");
}

stack *stack_new() {
    stack *new = calloc(1, sizeof(stack));
    new->head = calloc(1, sizeof(list));
    new->tail = new->head;
    return new;
}

void push(stack *S, size_t score, char ch, bool is_char) {
    list *append = calloc(1, sizeof(list));
    if (is_char) append->ch = ch;
    else append->sc = score;
    append->next = S->head;
    S->head = append;
}

void pop(stack *S) {
    list *to_free = S->head;
    S->head = S->head->next;
    free(to_free);
}

void free_list(list *head, list *tail) {
    if (head == tail) free(head);
    else {
        free_list(head->next, tail);
        free(head);
    }
}

void free_stack(stack *S) {
    free_list(S->head, S->tail);
    free(S);
}

int main() {
    const char *file = "chunks.txt";
    FILE *f = fopen(file, "r");
    char *line = NULL;
    size_t n = 0;

    stack *scores = stack_new();
    size_t num_wrong = 0;

    while (getline(&line, &n, f) != EOF) {
        stack *chars = stack_new();
        bool no_err = true;

        for (size_t i = 0; line[i] != '\n' && no_err; i++) {
            char top = chars->head->ch;
            char c = line[i];
            if (c == '(' || c == '{' || c == '[' || c == '<')
                push(chars, 0, c, true);
            else if ((c == ')' && top != '(') || (c == '}' && top != '{')
                    || (c == '>' && top != '<') || (c == ']' && top != '['))
                no_err = false;
            else
                pop(chars);
        }
        if (no_err) {
            num_wrong++;
            size_t score = 0;
            for (list *cur = chars->head; cur != chars->tail; cur = cur->next) {
                score *= 5;
                char c = cur->ch;
                if (c == '(') score += 1;
                if (c == '[') score += 2;
                if (c == '{') score += 3;
                if (c == '<') score += 4;
            }
            list *new = calloc(1, sizeof(list));
            new->sc = score;
            bool not_found = true;
            list *cur = scores->head;
            list *prev = NULL;
            while (cur != scores->tail && not_found) {
                if (score < cur->sc) {
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
                scores->tail->sc = score;
                scores->tail->next = new;
                scores->tail = new;
            }
        }
        free_stack(chars);
    }

    list *cur = scores->head;
    for (size_t i = 0; i < num_wrong / 2; i++)
        cur = cur->next;
    printf("Answer: %zu\n", cur->sc);
    free_stack(scores);
    free(line);
    fclose(f);
    return 0;
}
