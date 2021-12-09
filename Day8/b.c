#define _GNU_SOURCE
#include <assert.h>
#include <limits.h>
#include <stdint.h>
#include <stdbool.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

const size_t num_digits = 10;
const size_t num_pos = 7;
const size_t num_tests = 6;
// const bool screens[10][7] = {
//     {true, true, true, false, true, true, true},
//     {false, false, true, false, false, true, false},
//     {true, false, true, true, true, false, true},
//     {true, false, true, true, false, true, true},
//     {false, true, true, true, false, true, false},
//     {true, true, false, true, false, true, true},
//     {true, true, false, true, true, true, true},
//     {true, false, true, false, false, true, false},
//     {true, true, true, true, true, true, true},
//     {true, true, true, true, false, true, true}
// };
const bool easy[3][7] = {
    {false, false, true, false, false, true, false},
    {true, false, true, false, false, true, false}
};

/**
 * My Positions 
 *  0
 * 1 2
 *  3
 * 4 5
 *  6
 */

void print_wires(bool wires[num_pos][num_tests]) {
    for (size_t i = 0; i < num_pos; i++) {
        for (size_t j = 0; j < num_tests; j++)
            printf("%d ", wires[i][j]);
        printf("\n");
    }
    printf("\n");
}

void print_posses(bool posses[num_pos][num_pos]) {
    for (size_t i = 0; i < num_pos; i++) {
        for (size_t j = 0; j < num_tests; j++)
            printf("%d ", posses[i][j]);
        printf("\n");
    }
    printf("\n");
}

void init(bool wires[num_pos][num_pos], bool start) {
    for (size_t i = 0; i < num_pos; i++)
        for (size_t j = 0; j < num_pos; j++)
            wires[i][j] = start;
}

// Removes the possibilities of the possible positions of wires
void rem_easy(bool wires[num_pos][num_tests], bool posses[num_pos][num_pos],
              size_t pos, size_t tester) {
    for (size_t i = 0; i < num_pos; i++)
        if (wires[pos][tester] ^ easy[tester][i])
            posses[pos][i] = false;
}

void rem_hard(bool wires[num_pos][num_tests], bool posses[num_pos][num_pos],
              size_t pos, size_t tester) {
    size_t x = 0;
}

int main() {
    const char *file = "displays.txt";
    FILE *f = fopen(file, "r");
    char *line = NULL;
    size_t n = 0;

    while (getline(&line, &n, f) != EOF) {
        bool wires[num_pos][num_tests];
        init(wires, false);

        char *temp = line;
        char *tok = strtok(temp, " ");
        while (tok[0] != '|') {
            size_t len = strlen(tok);
            for (size_t i = 0; i < len; i++)
                wires[tok[i] - 'a'][len - 2] = true;
            tok = strtok(NULL, " ");
        }
        bool posses[num_pos][num_pos];
        init(posses, true);
        for (size_t tries = 0; tries < 8; tries++) {
            for (size_t i = 0; i < num_pos; i++)
                for (size_t j = 0; j < 2; j++)
                    rem_easy(wires, posses, i, j);
        }
        // print_wires(wires);
        print_posses(posses);

        printf("\n");
    }

    printf("Answer: %zu\n", (size_t)0);
    free(line);
    fclose(f);
    return 0;
}
