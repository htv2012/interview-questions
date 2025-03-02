#ifndef COMMON_H_339BE7E
#define COMMON_H_339BE7E

#include <iostream>
#include <climits>
#include <gtest/gtest.h>
#include <List.h>

using namespace std;

class ListTest : public testing::Test {
public:
protected:
    List list;
	virtual void SetUp();
	virtual void TearDown();
};

List* createListOfLength(unsigned int n);

#endif // COMMON_H_339BE7E
