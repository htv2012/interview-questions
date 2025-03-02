/***********************************************************************
* HEADER
***********************************************************************/

#include <iostream>
#include <gtest/gtest.h>
#include "SqueezeSpaces.h"

using namespace std;

class SqueezeSpacesTest : public testing::Test{
public:
    // virtual void SetUp();
    void performTest(const char *actual, const char *expected);
    char buffer[1024];
};

/***********************************************************************
* TESTS
***********************************************************************/

TEST_F(SqueezeSpacesTest, onlySingleSpace) {
    performTest(
        "A day like any other day.", 
        "A day like any other day.");
}
TEST_F(SqueezeSpacesTest, singleSpaceInFront) {
    performTest(" ab cd", "ab cd");
}
TEST_F(SqueezeSpacesTest, singleSpaceAfter) {
    performTest("A day without rain ", "A day without rain ");
}
TEST_F(SqueezeSpacesTest, emptyString) {
    performTest("", "");
}
TEST_F(SqueezeSpacesTest, nullPointer) {
    SqueezeSpaces(NULL);
}
TEST_F(SqueezeSpacesTest, oneSpace) {
    performTest(" ", "");
}
TEST_F(SqueezeSpacesTest, spacesOnly) {
    performTest("    ", "");
}

TEST_F(SqueezeSpacesTest, multipleInFront) {
    performTest("    Once upon a time", "Once upon a time");
}
TEST_F(SqueezeSpacesTest, multipleAtEnd) {
    performTest("Once upon a time   ", "Once upon a time");
}
TEST_F(SqueezeSpacesTest, multipleInMiddle) {
    performTest("Once  upon   a    time", "Once upon a time");
}
TEST_F(SqueezeSpacesTest, multipleInAll) {
    performTest("    Once  upon   a    time ", "Once upon a time");
}

/***********************************************************************
* TEST SUPPORT
***********************************************************************/

void SqueezeSpacesTest::performTest(const char *actual, const char *expected) {
    strcpy(buffer, actual);
    SqueezeSpaces(buffer);
    EXPECT_STREQ(expected, buffer);
}