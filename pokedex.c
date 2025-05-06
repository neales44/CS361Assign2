// pokedex.c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include "pokedex.h"

Pokemon pokedex[MAX_POKEMON];
int pokemon_count = 0;

static void to_lowercase(char* str) {
    while (*str) {
        *str = tolower(*str);
        str++;
    }
}

static void trim_newline(char* str) {
    size_t len = strlen(str);
    if (len > 0 && str[len-1] == '\n') str[len-1] = '\0';
}

void load_pokedex(const char* filename) {
    FILE* file = fopen(filename, "r");
    if (!file) {
        perror("Failed to open CSV file");
        exit(1);
    }

    char line[512];
    fgets(line, sizeof(line), file); // Skip header
    while (fgets(line, sizeof(line), file)) {
        if (pokemon_count >= MAX_POKEMON) break;
        Pokemon* p = &pokedex[pokemon_count];
        char* token = strtok(line, ",");
        p->number = atoi(token);

        token = strtok(NULL, ",");
        strncpy(p->name, token, sizeof(p->name));

        // Type field (quoted string: "['Fire', 'Flying']" or "['Psychic']")
        token = strtok(NULL, ",");
        char typefield[50];
        strncpy(typefield, token, sizeof(typefield));

        // Strip quotes and brackets
        char* inner = strchr(typefield, '[');
        if (inner) {
            inner++; // move past [
            char* end = strchr(inner, ']');
            if (end) *end = '\0';

            // Now inner contains: 'Fire', 'Flying' or 'Psychic'
            char* type_token = strtok(inner, "'");
            int found = 0;
            while (type_token && found < 2) {
                if (type_token[0] != ',' && type_token[0] != ' ') {
                    if (found == 0)
                        strncpy(p->type1, type_token, sizeof(p->type1));
                    else
                        strncpy(p->type2, type_token, sizeof(p->type2));
                    found++;
                }
                type_token = strtok(NULL, "'");
            }
            if (found == 1)
                strcpy(p->type2, "None");
        } else {
            strcpy(p->type1, "Unknown");
            strcpy(p->type2, "None");
        }

        token = strtok(NULL, ","); p->total = atoi(token);
        token = strtok(NULL, ","); p->hp = atoi(token);
        token = strtok(NULL, ","); p->attack = atoi(token);
        token = strtok(NULL, ","); p->defense = atoi(token);
        token = strtok(NULL, ","); p->sp_atk = atoi(token);
        token = strtok(NULL, ","); p->sp_def = atoi(token);
        token = strtok(NULL, ","); p->speed = atoi(token);
        token = strtok(NULL, ","); p->generation = atoi(token);
        token = strtok(NULL, ","); if (token) trim_newline(token); p->legendary = token && strcmp(token, "True") == 0;

        pokemon_count++;
    }

    fclose(file);
}




void view_all_pokemon() {
    for (int i = 0; i < pokemon_count; i++) {
        printf("%03d - %s (%s/%s)\n", pokedex[i].number, pokedex[i].name, pokedex[i].type1, pokedex[i].type2);
    }
}

void search_by_type() {
    char input[20];
    printf("Enter a Pokemon type: ");
    fgets(input, sizeof(input), stdin);
    trim_newline(input);
    to_lowercase(input);

    printf("\nPokemon with type '%s':\n", input);
    for (int i = 0; i < pokemon_count; i++) {
        char type1[20], type2[20];
        strncpy(type1, pokedex[i].type1, sizeof(type1)); to_lowercase(type1);
        strncpy(type2, pokedex[i].type2, sizeof(type2)); to_lowercase(type2);

        if (strcmp(type1, input) == 0 || strcmp(type2, input) == 0) {
            printf("%03d - %s (%s/%s)\n", pokedex[i].number, pokedex[i].name, pokedex[i].type1, pokedex[i].type2);
        }
    }
}
