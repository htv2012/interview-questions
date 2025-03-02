#include "linkedlist.h"
#include <stdio.h>

node *list_find_nth_node_from_tail(node *head, int n) {
    node* front = head;
    node* rear = head;

    // Advance the front pointer n nodes
    for (; n && front; --n, front = front->next) 
        ;
    if (!front) return EMPTY_NODE;
    
    // Move both the front and the rear in sync until front reaches
    // the end.
    while (front->next) {
        front = front->next;
        rear = rear->next;
    }

    return rear;
}

