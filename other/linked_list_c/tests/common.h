#ifndef COMMON_H_339BE7E
#define COMMON_H_339BE7E

#include <iostream>
#include <climits>
#include <gtest/gtest.h>
#include <linkedlist.h>


class ListTest : public testing::Test {
public:
	node *list;
protected:
	virtual void SetUp();
	virtual void TearDown();
    node* createListOfLength(int n);
    void clearList(node **list);
};

#endif
