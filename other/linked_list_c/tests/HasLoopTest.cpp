#include "common.h"

/**********************************************************************
 * Test fixture
 */

class HasLoopTest : public ListTest {
protected:
    node *lastNode;

public:
    void createLoopAtNodeNumber(int nodeNumber) {
        int count;
        node *marker;

        // Put a marker where the last node loops back to. If nodeNumber
        // exceeds the length of the list, marker will be NULL
        for (count = 1, marker = list; marker; marker = marker->next)
            if (count++ == nodeNumber) break;

        // Seeks to the last node, point its next pointer to the marker.
        // This will create a loop
        for (lastNode = marker; lastNode->next; lastNode = lastNode->next)
            ;
        lastNode->next = marker;
    }

    void undoCreateLoop() {
        lastNode->next = NULL;
    }
};

/**********************************************************************
 * Tests
 */

TEST_F(HasLoopTest, emptyList_ExpectFalse) {
	ASSERT_EQ(0, list_has_loop(list));
}

TEST_F(HasLoopTest, oneNodeWithoutLoop_ExpectFalse) {
    list = createListOfLength(1);
    ASSERT_EQ(0, list_has_loop(list));
}

TEST_F(HasLoopTest, oneNodeWithLoop_ExpectTrue) {
    list = createListOfLength(1);
    list->next = list;
    ASSERT_EQ(1, list_has_loop(list));
    list->next = EMPTY_NODE;
}

TEST_F(HasLoopTest, two_nodes_without_loop_ExpectFalse) {
    list = createListOfLength(2);
    ASSERT_EQ(0, list_has_loop(list));
}

TEST_F(HasLoopTest, two_nodes_loop_at_node_one_ExpectTrue) {
    list = createListOfLength(2);
    createLoopAtNodeNumber(1);
    ASSERT_EQ(1, list_has_loop(list));
    undoCreateLoop();
}

TEST_F(HasLoopTest, two_nodes_loop_at_node_two_ExpectTrue) {
    list = createListOfLength(2);
    createLoopAtNodeNumber(2);
    ASSERT_EQ(1, list_has_loop(list));
    list->next->next = NULL;
}

TEST_F(HasLoopTest, twenty_nodes) {
    list = createListOfLength(20);
    ASSERT_EQ(0, list_has_loop(list));

    createLoopAtNodeNumber(6);
    ASSERT_EQ(1, list_has_loop(list));
    undoCreateLoop();
}

TEST_F(HasLoopTest, loop_at_last_node) {
    list = createListOfLength(5);
    ASSERT_EQ(0, list_has_loop(list));
    
    createLoopAtNodeNumber(5);
    ASSERT_EQ(1, list_has_loop(list));
    undoCreateLoop();
}

TEST_F(HasLoopTest, loop_at_first_node) {
    list = createListOfLength(10);
    createLoopAtNodeNumber(1);
    ASSERT_EQ(1, list_has_loop(list));
    undoCreateLoop();
}
