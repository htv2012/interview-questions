#include "linkedlist.h"

node *get_value_then_advance(node **p) {
    node *current_node = *p;
    *p = (*p)->next;
    return current_node;
}

void list_merge_two_halves(node **head) {
    node *fh = *head;
    node *sh;
    node *tail;

    // Advance until list becomes unsorted. That will be the start of
    // the second list.
    while (fh && fh->next && fh->data <= fh->next->data) {
        fh = fh->next;
    }

    // If list is already sorted, or empty, return right away
    if (fh == EMPTY_NODE || fh->next == EMPTY_NODE) return;

    // At this point fh points to the last node of the first half.
    // Split the list into two, fh points the the first half, and sh
    // points to the second half.
    sh = fh->next;
    fh->next = EMPTY_NODE;
    fh = *head;

    // Merge the very first node
    if (fh->data <= sh->data) {
        *head = get_value_then_advance(&fh);
    } else {
        *head = get_value_then_advance(&sh);
    }

    // Merge the rest of the lists
    for (tail = *head; fh && sh;) {
        if (fh->data <= sh->data) {
            tail->next = fh;
            tail = get_value_then_advance(&fh);
        } else {
            tail->next = sh;
            tail = get_value_then_advance(&sh);
        }
    }
    tail->next = fh ? fh : sh;
}

