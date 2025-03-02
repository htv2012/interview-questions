#include "List.h"

void List::push_back(const int& value) {
    List::Node* new_node = new List::Node(value);
    if (_head) {
        _tail->next = new_node;
        _tail = new_node;
    } else {
        _head = new_node;
        _tail = new_node;
    }
    _size++;
}
