#ifndef COMMON_H_339BE7E
#define COMMON_H_339BE7E

#include <iostream>
#include <climits>
#include <linkedlist.h>
#include <cxxtest/TestSuite.h>

class ListTest {
public:
    node* createListOfLength(int n);
    void clearList(node **list);
};

#endif
