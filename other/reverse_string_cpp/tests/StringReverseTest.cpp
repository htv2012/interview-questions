/***********************************************************************
* HEADER
***********************************************************************/

#include <iostream>
#include <gtest/gtest.h>
#include "StringReverse.h"

using namespace std;

class StringReverseTest : public testing::Test{
public:
    // virtual void SetUp();
    void performTest(const char *actual, const char *expected);
    char buffer[1024];
};

/***********************************************************************
* TESTS
***********************************************************************/

TEST_F(StringReverseTest, oddLength) {
    performTest("abcde", "edcba");
}
TEST_F(StringReverseTest, evenLength) {
    performTest("abcd", "dcba");
}
TEST_F(StringReverseTest, singleChar) {
    performTest("x", "x");
}
TEST_F(StringReverseTest, emptyString) {
    performTest("", "");
}
TEST_F(StringReverseTest, nullPointer) {
    StringReverse(NULL);
}

/***********************************************************************
* TEST SUPPORT
***********************************************************************/

void StringReverseTest::performTest(const char *actual, const char *expected) {
    cout << 1 << endl;
    strcpy(buffer, actual);
    cout << 2 << endl;
    StringReverse(buffer);
    EXPECT_STREQ(expected, buffer);
}