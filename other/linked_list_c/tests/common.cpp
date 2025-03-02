
#include "common.h"

node* ListTest::createListOfLength(int n) {
    node *list = EMPTY_NODE;
    for (int i = 0; i < n; i++) {
        list_append(&list, i);
    }
    return list;
}

void ListTest::clearList(node **list) {
    if (*list == NULL) return;
    node *temp;
    for (; *list != NULL; *list = temp) {
        temp = (*list)->next;
        free(*list);
    }
    *list = EMPTY_NODE;
}

void ListTest::SetUp() {
    list = EMPTY_NODE;
}

void ListTest::TearDown() {
    clearList(&list);
}
