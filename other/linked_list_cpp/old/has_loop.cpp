#include "List.h"

/* This is Brent's algorithm */
bool List::has_loop() {
    List::Node* turtle = NULL;
    List::Node* hare = _head;
    unsigned int steps_taken = 0;
    unsigned int steps_to_take = 2;

    while (hare && hare != turtle) {
        if (steps_taken == steps_to_take) {
            turtle = hare;
            steps_taken = 0;
            steps_to_take *= 2;
        }
        hare = hare->next;
        ++steps_taken;
    }
    return (hare != NULL);
}
