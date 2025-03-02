#include "common.h"

/**********************************************************************
 * Test fixture
 */

class LengthTest : public ListTest {
};

/**********************************************************************
 * Tests
 */

TEST_F(LengthTest, emptyList_ExpectZero) {
    EXPECT_EQ(0, list_length(list));
}

TEST_F(LengthTest, listOfOne_ExpectOne) {
    list = createListOfLength(1);
    EXPECT_EQ(1, list_length(list));
}

TEST_F(LengthTest, ListOfTwo_ExpectTwo) {
    list = createListOfLength(2);
    EXPECT_EQ(2, list_length(list));
}

TEST_F(LengthTest, ListOfThree_ExpectThree) {
    list = createListOfLength(3);
    EXPECT_EQ(3, list_length(list));
}

TEST_F(LengthTest, ListOf99_Expect99) {
	list = createListOfLength(99);
    EXPECT_EQ(99, list_length(list));
}

TEST_F(LengthTest, ListOfMany_ExpectCorrectResult) {
	const int LIST_LENGTH = 9999;
	list = createListOfLength(LIST_LENGTH);
    EXPECT_EQ(LIST_LENGTH, list_length(list));
}