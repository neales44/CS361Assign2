// stat_game.c
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "pokedex.h"
#include "stat_game.h"

void play_stat_guessing_game() {
    srand(time(NULL));
    int index = rand() % pokemon_count;
    Pokemon* p = &pokedex[index];

    printf("\nGuess the HP of %s (%s/%s): ", p->name, p->type1, p->type2);

    int guess;
    scanf("%d", &guess);
    getchar();

    if (guess == p->hp) {
        printf("Correct! %s has %d HP.\n", p->name, p->hp);
    } else {
        printf("Wrong. %s has %d HP, not %d.\n", p->name, p->hp, guess);
    }
}
