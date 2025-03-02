#include "List.h"

void List::reverse() {
    List::Node* previous = NULL;
    List::Node* current = _head;
    List::Node* next;

    _tail = _head;
    while (current) {
        next = current->next;
        current->next = previous;
        previous = current;
        current = next;
    }
    _head = previous;
}