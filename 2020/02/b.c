#include <stdlib.h>
#include <stdio.h>
#include <string.h>


int main() {
    const char *filename = "passwords.txt";
    FILE *f = fopen(filename, "r");
    char *line = NULL;
    size_t n = 0;
    size_t valids = 0;
    while (getline(&line, &n, f) != -1) {
        char *temp = line;
        char *str = strchr(line, ':');
        size_t num_digits = strlen(str) - 3;
        char *pass = calloc(sizeof(char), num_digits + 1);
        strncpy(pass, &str[2], num_digits);
        size_t i = (size_t)strtol(temp, &temp, 10);
        temp++;
        size_t j = (size_t)strtol(temp, &temp, 10);
        char c = temp[1];

        if ((pass[i - 1] == c) ^ (pass[j - 1] == c))
            valids++;
        
        free(pass);
    }

    printf("Answer: %zu\n", valids);
    free(line);
    fclose(f);

    return 0;
}