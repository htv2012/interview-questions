
#include "common.h"

List* createListOfLength(unsigned int n) {
    List* list = new List();
    for (int i = 0; i < n; i++) {
        list->push_back(i);
    }
    return list;
}

void ListTest::SetUp() {
}

void ListTest::TearDown() {
}
