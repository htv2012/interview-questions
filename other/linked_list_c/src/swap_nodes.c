#include "linkedlist.h"

int list_swap_nodes(node* head, int n) {
    node* nth_from_head;
    node* nth_from_tail;
    node* tail;
    int i;

    // Locate the Nth node from the head
    for (i = 1, nth_from_head = head; i < n && nth_from_head; i++) {
        nth_from_head = nth_from_head->next;
    }

    // Error conditions:
    // 1. n < 1: n is too small
    // 2. nth_from_head == NULL: either head==NULL, or n is too big
    if (n < 1 || !nth_from_head) {
        return LIST_INVALID_PARAMETER;
    }

    // Locate the Nth node from the tail
    for (nth_from_tail = head, tail = nth_from_head; tail->next;) {
        tail = tail->next;
        nth_from_tail = nth_from_tail->next;
    }

    // Swap them, just swap the data
    i = nth_from_head->data;
    nth_from_head->data = nth_from_tail->data;
    nth_from_tail->data = i;

    return LIST_OK;
}

