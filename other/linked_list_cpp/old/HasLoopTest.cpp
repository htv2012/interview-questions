#include "common.h"

/**********************************************************************
 * Test fixture
 */

class HasLoopTest: 
        public ::testing::TestWithParam< unsigned int > {
public:
    virtual void TearDown() { delete list; }
    virtual void SetUp() {
        numberOfNodes = (unsigned int)GetParam();
        cout << "Setup: number of nodes: " << numberOfNodes << endl;
        list = createListOfLength(numberOfNodes);
        cout << "List: ";
        for (List::iterator it=list->begin(); it!=list->end(); it++) {
            cout << *it << " ";
        }
        cout << endl;
    }

    void debug_node(List::Node* node, const char* label) {
        cout << label << node << "(" << node->data << ")"
            << "->" << node->next << endl;

    }

    /* node number 0 is the first node */
    void createLoopAtNodeNumber(unsigned int nodeNumber) {
        marker = list->get_head();
        debug_node(marker, "Marker: ");

        for (unsigned int i = 0; i < nodeNumber; i++) {
            marker = marker->next;
        }

        List::Node* tail = list->get_tail();
        debug_node(tail, "Tail: ");
        tail->next = marker;

        // DEBUG
        cout << "List with loop: ";
        List::Node *node = list->get_head();
        int count = 0;
        for (; count < 2; node = node->next) {
            cout << node->data << " ";
            if (node == marker) { ++count; }
        }
        cout << endl;
    }

    void undoCreateLoop() {
        List::Node* tail = list->get_tail();
        debug_node(tail, "Undo, tail: ");
        tail->next = NULL;
    }

protected:
    List* list;
    List::Node* marker;
    unsigned int numberOfNodes;
};

/**********************************************************************
 * Tests
 */

TEST(HasLoopOddCasesTest, EmptyList) {
    List list;
    ASSERT_FALSE(list.has_loop());
}

// Test parameter: number of nodes
TEST_P(HasLoopTest, NoLoop) {
    ASSERT_FALSE(list->has_loop());
}

TEST_P(HasLoopTest, HasLoop) {
    for (unsigned int n = 0; n < numberOfNodes; n++) {
        createLoopAtNodeNumber(n);
        EXPECT_TRUE(list->has_loop());
        undoCreateLoop();
    }
}

INSTANTIATE_TEST_CASE_P(
    GeneralCases,
    HasLoopTest,
    ::testing::Range(3U, 21U));

INSTANTIATE_TEST_CASE_P(
    CornerCases,
    HasLoopTest,
    ::testing::Values(1U, 2U));
