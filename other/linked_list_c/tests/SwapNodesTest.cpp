#include "common.h"
using namespace std;

/**********************************************************************
 * Test fixture
 */

class SwapNodesTest : public ListTest {
public:
    void debugInfo(int listLength, int n, int expectedReturn, int expectedElements[]) {
        return; // no debug info
        cout << "List length:     " << listLength << endl;
        cout << "n:               " << n << endl;
        cout << "Expected Return: " << expectedReturn << endl;
        if (expectedReturn != LIST_OK) { return; }

        cout << "Expected:        ";
        for (int i = 0; i < listLength; i++) {
            cout << expectedElements[i] << " ";
        }
        cout << endl;

        cout << "Actual:          ";
        for (node* p = list; p; p = p->next) {
            cout << p->data << " ";
        }
        cout << endl;
    }

	void doTest(int listLength, int n, int expectedReturn, int expectedElements[]) {
        list = createListOfLength(listLength);

        int actualReturn = list_swap_nodes(list, n);
        debugInfo(listLength, n, expectedReturn, expectedElements);
        EXPECT_EQ(expectedReturn, actualReturn);

        if (expectedElements) {
            node* current = list;
            for (int i = 0; i < listLength; i++) {
                //cout << "[" << i << "]: " << expectedElements[i] << ", " << current->data << endl;
                EXPECT_EQ(expectedElements[i], current->data);
                current = current->next;
            }
        }
    }
};

/**********************************************************************
 * Tests
 */

TEST_F(SwapNodesTest, emptyListNEquals0) {
	doTest(0, 0, LIST_INVALID_PARAMETER, NULL);
}

TEST_F(SwapNodesTest, emptyListNNegative) {
	doTest(0, -1, LIST_INVALID_PARAMETER, NULL);	
}

TEST_F(SwapNodesTest, emptyListNPositive) {
	doTest(0, 2, LIST_INVALID_PARAMETER, NULL);	
}

TEST_F(SwapNodesTest, nTooBig) {
	doTest(5, 6, LIST_INVALID_PARAMETER, NULL);
}

TEST_F(SwapNodesTest, nNegative) {
    doTest(5, -3, LIST_INVALID_PARAMETER, NULL);
}

TEST_F(SwapNodesTest, nEqual1) {
    int expectedElements[] = {4, 1, 2, 3, 0};
	doTest(5, 1, LIST_OK, expectedElements);
}

TEST_F(SwapNodesTest, nEqualListLength) {
    int expectedElements[] = {4, 1, 2, 3, 0};
	doTest(5, 5, LIST_OK, expectedElements);
}

TEST_F(SwapNodesTest, nEqualsListLengthMinus1) {
    int expectedElements[] = {0, 7, 2, 3, 4, 5, 6, 1, 8};
	doTest(9, 8, LIST_OK, expectedElements);
}

TEST_F(SwapNodesTest, nIsLessThanHalfOfListLength) {
    int expectedElements[] = {0, 1, 6, 3, 4, 5, 2, 7, 8};
	doTest(9, 3, LIST_OK, expectedElements);
}

TEST_F(SwapNodesTest, nIsMoreThanHalfOfListLength) {
    int expectedElements[] = {0, 1, 2, 5, 4, 3, 6, 7, 8};
	doTest(9, 6, LIST_OK, expectedElements);
}

TEST_F(SwapNodesTest, swapSameNode) {
    int expectedElements[] = {0, 1, 2, 3, 4, 5, 6, 7, 8};
	doTest(9, 5, LIST_OK, expectedElements);
}

TEST_F(SwapNodesTest, nIsZero) {
	doTest(4, 0, LIST_INVALID_PARAMETER, NULL);
}

TEST_F(SwapNodesTest, nIs1) {
    int expectedElements[] = {4, 1, 2, 3, 0};
	doTest(5, 1, LIST_OK, expectedElements);
}
