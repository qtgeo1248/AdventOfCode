#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <stdbool.h>
#include <ctype.h>

bool is_pass(bool* info) {
    for (int i = 0; i < 7; i++)
        if (!info[i]) return false;
    return true;
}

char *get_field(size_t *n, FILE *f) { // Assumes just got a ':' char
    char *field = calloc(sizeof(char), 20);
    size_t i = 0;
    for (int cur = fgetc(f); cur != ' ' && cur != '\n'; cur = fgetc(f)) {
        field[i] = (char)cur;
        i++;
    }
    *n = i;
    return field;
}

bool is_hair_color(char *field, size_t n) {
    if (field[0] != '#') return false;
    for (size_t i = 1; i < n; i++)
        if ((field[i] < '0' || '9' < field[i])
            && (field[i] < 'a' || 'f' < field[i]))
            return false;
    return true;
}

bool is_eye_color(char *field) {
    return strcmp(field, "amb") == 0 || strcmp(field, "blu") == 0
        || strcmp(field, "brn") == 0 || strcmp(field, "gry") == 0
        || strcmp(field, "grn") == 0 || strcmp(field, "hzl") == 0
        || strcmp(field, "oth") == 0;
}

bool is_pid(char *field, size_t n) {
    if (n != 9) return false;
    for (size_t i = 0; i < n; i++) {
        if (!isdigit(field[i])) return false;
    }
    return true;
}

int main() {
    const char *filename = "tests/testB1.txt";
    FILE *f = fopen(filename, "r");
    size_t count = 0;

    bool *valids = calloc(sizeof(bool), 7);
    char *curs = calloc(sizeof(char), 3);

    for (int cur = fgetc(f); cur != EOF; cur = fgetc(f)) {
        if (cur == ':') {
            size_t n;
            char *field = get_field(&n, f);
            switch (curs[0] + curs[1] + curs[2]) {
                case 333: { // byr
                    char *tmp = NULL;
                    long byr = strtol(field, &tmp, 10);
                    if (1920 <= byr && byr <= 2002)
                        valids[0] = true;
                    break;
                } case 340: { // iyr
                    char *tmp = NULL;
                    long iyr = strtol(field, &tmp, 10);
                    if (2010 <= iyr && iyr <= 2020)
                        valids[1] = true;
                    break;
                } case 336: { // eyr
                    char *tmp = NULL;
                    long eyr = strtol(field, &tmp, 10);
                    if (2020 <= eyr && eyr <= 2030)
                        valids[2] = true;
                    break;
                } case 323: { // hgt
                    char *tmp = NULL;
                    long hgt = strtol(field, &tmp, 10);
                    if ((strcmp(tmp, "cm") == 0 && 150 <= hgt && hgt <= 193)
                        || (strcmp(tmp, "in") == 0 && 59 <= hgt && hgt <= 76))
                        valids[3] = true;
                    break;
                } case 311: { // hcl
                    if (is_hair_color(field, n))
                        valids[4] = true;
                    break;
                } case 308: { // ecl
                    if (is_eye_color(field))
                        valids[5] = true;
                    break;
                } case 317: { // pid
                    if (is_pid(field, n))
                        valids[6] = true;
                    break;
                }
                // cid (don't do anything)
            }
            free(field);
        }
        
        if (cur == '\n') {
            if (is_pass(valids)) count++;
            free(valids);
            valids = calloc(sizeof(bool), 7);
        }
        curs[0] = curs[1];
        curs[1] = curs[2];
        curs[2] = (char)cur;
    }

    printf("Answer: %zu\n", count);

    free(valids);
    free(curs);
    fclose(f);

    return 0;
}