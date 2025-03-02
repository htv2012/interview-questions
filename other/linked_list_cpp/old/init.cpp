#include "List.h"

List::Node::Node() {
    data = 0;
    next = NULL;
}

List::Node::Node(int new_data, List::Node *next_node) {
    data = new_data;
    next = next_node;
}

List::List():_head(NULL), _tail(NULL), _size(0) {}

List::~List() {
    List::Node *current;
    while (_head) {
        current = _head;
        _head = _head->next;
        delete current;
    }
}