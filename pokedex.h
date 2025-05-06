// pokedex.h
#ifndef POKEDEX_H
#define POKEDEX_H

#define MAX_POKEMON 1000

typedef struct {
    int number;
    char name[50];
    char type1[20];
    char type2[20];
    int total, hp, attack, defense, sp_atk, sp_def, speed, generation;
    int legendary;
} Pokemon;

extern Pokemon pokedex[MAX_POKEMON];
extern int pokemon_count;

void load_pokedex(const char* filename);
void view_all_pokemon();
void search_by_type();

#endif
