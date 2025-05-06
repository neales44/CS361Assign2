// main.c
#include <stdio.h>
#include "pokedex.h"
#include "stat_game.h"

void show_menu() {
    printf("\n=== Pokemon Game Menu ===\n");
    printf("1. View All Pokemon\n");
    printf("2. Search Pokemon by Type\n");
    printf("3. Play Stat Guessing Game\n");
    printf("4. Exit\n");
}

int main() {
    load_pokedex("pokePd.csv");

    int choice;
    do {
        show_menu();
        printf("Choose an option: ");
        scanf("%d", &choice);
        getchar(); // consume newline

        switch (choice) {
            case 1:
                view_all_pokemon();
                break;
            case 2:
                search_by_type();
                break;
            case 3:
                play_stat_guessing_game();
                break;
            case 4:
                printf("Exiting. Goodbye!\n");
                break;
            default:
                printf("Invalid option. Try again.\n");
        }
    } while (choice != 4);

    return 0;
}
