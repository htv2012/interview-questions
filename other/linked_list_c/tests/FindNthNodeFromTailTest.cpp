#include "common.h"

/**********************************************************************
 * Test fixture
 */

class FindNthNodeFromTailTest : public ListTest {
public:
    node *nth_node;
};

/**********************************************************************
 * Tests
 */

TEST_F(FindNthNodeFromTailTest, ShouldRejectNegativeCount) {
    list = createListOfLength(10);
    nth_node = list_find_nth_node_from_tail(list, -3);
    ASSERT_TRUE(nth_node == EMPTY_NODE);
}

TEST_F(FindNthNodeFromTailTest, EmptyListNIsPositive) {
    nth_node = list_find_nth_node_from_tail(list, 5);
    ASSERT_TRUE(nth_node == EMPTY_NODE);
}

TEST_F(FindNthNodeFromTailTest, EmptyListNIsNegative) {
    nth_node = list_find_nth_node_from_tail(list, -3);
    ASSERT_TRUE(nth_node == EMPTY_NODE);
}

TEST_F(FindNthNodeFromTailTest, EmptyListNIsZero) {
    nth_node = list_find_nth_node_from_tail(list, 0);
    ASSERT_TRUE(nth_node == EMPTY_NODE);
}

TEST_F(FindNthNodeFromTailTest, GetLastNode) {
    list = createListOfLength(10);
    nth_node = list_find_nth_node_from_tail(list, 0);
    ASSERT_FALSE(EMPTY_NODE == nth_node);
    ASSERT_EQ(9, nth_node->data);
}

TEST_F(FindNthNodeFromTailTest, GetNextToLastNode) {
    list = createListOfLength(10);
    nth_node = list_find_nth_node_from_tail(list, 1);
    ASSERT_FALSE(EMPTY_NODE == nth_node);
    ASSERT_EQ(8, nth_node->data);
}

TEST_F(FindNthNodeFromTailTest, GetMiddleNode) {
    list = createListOfLength(10);
    nth_node = list_find_nth_node_from_tail(list, 5);
    ASSERT_NE(EMPTY_NODE, nth_node);
    ASSERT_EQ(4, nth_node->data);
}

TEST_F(FindNthNodeFromTailTest, GetFirstNode) {
    list = createListOfLength(10);
    nth_node = list_find_nth_node_from_tail(list, 9);
    ASSERT_FALSE(EMPTY_NODE == nth_node);
    ASSERT_EQ(0, nth_node->data);
    ASSERT_EQ(list, nth_node);
}

TEST_F(FindNthNodeFromTailTest, ListTooShort) {
    list = createListOfLength(10);
    nth_node = list_find_nth_node_from_tail(list, 10);
    ASSERT_TRUE(EMPTY_NODE == nth_node);
}

TEST_F(FindNthNodeFromTailTest, ReturnFirstNode) {
    list = createListOfLength(5);
    nth_node = list_find_nth_node_from_tail(list, 4);
    ASSERT_NE(EMPTY_NODE, nth_node);
    ASSERT_EQ(0, nth_node->data);
}

TEST_F(FindNthNodeFromTailTest, ListOneNodeTooShort) {
    list = createListOfLength(5);
    nth_node = list_find_nth_node_from_tail(list, 5);
    ASSERT_TRUE(EMPTY_NODE == nth_node);
}

TEST_F(FindNthNodeFromTailTest, OneNodeGetLastNode) {
    list = createListOfLength(1);
    nth_node = list_find_nth_node_from_tail(list, 0);
    ASSERT_FALSE(EMPTY_NODE == nth_node);
    ASSERT_EQ(0, nth_node->data);
}

TEST_F(FindNthNodeFromTailTest, OneNodeListTooShort) {
    list = createListOfLength(1);

    nth_node = list_find_nth_node_from_tail(list, 1);
    ASSERT_TRUE(EMPTY_NODE == nth_node);
}

TEST_F(FindNthNodeFromTailTest, TwoNodesGetLastNode) {
    list = createListOfLength(2);
    nth_node = list_find_nth_node_from_tail(list, 0);
    ASSERT_FALSE(EMPTY_NODE == nth_node);
    ASSERT_EQ(1, nth_node->data);
}

TEST_F(FindNthNodeFromTailTest, TwoNodesGetFirstNode) {
    list = createListOfLength(2);

    nth_node = list_find_nth_node_from_tail(list, 1);
    ASSERT_FALSE(EMPTY_NODE == nth_node);
    ASSERT_EQ(0, nth_node->data);
    ASSERT_EQ(list, nth_node);
}

TEST_F(FindNthNodeFromTailTest, TwoNodesListTooShort) {
    list = createListOfLength(2);

    nth_node = list_find_nth_node_from_tail(list, 2);
    ASSERT_TRUE(EMPTY_NODE == nth_node);
}

