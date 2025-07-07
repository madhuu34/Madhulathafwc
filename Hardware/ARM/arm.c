#include <stdio.h>

int main() {
    // Given values
    int total_persons = 25;
    int play_hockey = 15;
    int play_football = 17;
    int play_both = 10;

    // Calculate the number of persons playing at least one sport (hockey OR football)
    // Using the principle of inclusion-exclusion:
    // |A U B| = |A| + |B| - |A intersection B|
    int play_at_least_one = play_hockey + play_football - play_both;

    // Calculate the number of persons playing neither sport
    // Neither = Total - (Persons playing at least one)
    int play_neither = total_persons - play_at_least_one;

    printf("Total persons in the room: %d\n", total_persons);
    printf("Persons playing hockey: %d\n", play_hockey);
    printf("Persons playing football: %d\n", play_football);
    printf("Persons playing both hockey and football: %d\n", play_both);
    printf("\n");
    printf("Persons playing at least one sport (Hockey OR Football): %d\n", play_at_least_one);
    printf("Persons playing neither hockey nor football: %d\n", play_neither);

    return 0;
}
