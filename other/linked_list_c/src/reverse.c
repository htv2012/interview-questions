#include "linkedlist.h"

void list_reverse(node **head) {
    node *previous = EMPTY_NODE;
    node *current = *head;
    node *next;

    while (current) {
        next = current->next;
        current->next = previous;
        previous = current;
        current = next;
    }

    *head = previous;
}

