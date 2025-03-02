#include "common.h"

/**********************************************************************
 * Test fixture
 */

class ReverseTest : public ListTest {
public:
	void verifyReversedListOfLength(int n) {
		node *current = list;
		for (int i = 0; i < n; i++) {
			ASSERT_NE(EMPTY_NODE, current);
			EXPECT_EQ(n-i-1, current->data);
			current = current->next;
		}
	}
	
	void verifyListOfLength(int n) {
		node *current = list;
		for (int i = 0; i < n; i++) {
			ASSERT_NE(EMPTY_NODE, current);
			EXPECT_EQ(i, current->data);
			current = current->next;
		}
	}
};

/**********************************************************************
 * Tests
 */

TEST_F(ReverseTest, reverseEmptyList) {
	list_reverse(&list);
	ASSERT_EQ(EMPTY_NODE, list);
}

TEST_F(ReverseTest, reverseOneNode) {
	list_append(&list, 1);
	list_reverse(&list);
	ASSERT_NE(EMPTY_NODE, list);
	EXPECT_EQ(1, list->data);
}

TEST_F(ReverseTest, reverseTwoNodes) {
	list = createListOfLength(2);
	list_reverse(&list);
	verifyReversedListOfLength(2);
}

TEST_F(ReverseTest, reverseThreeNodes) {
	list = createListOfLength(3);
	list_reverse(&list);
	verifyReversedListOfLength(3);
}

TEST_F(ReverseTest, reverseFourNodes) {
	list = createListOfLength(4);
	list_reverse(&list);
	verifyReversedListOfLength(4);
}

TEST_F(ReverseTest, reverseTwice) {
	list = createListOfLength(5);
	list_reverse(&list);
	verifyReversedListOfLength(5);
	list_reverse(&list);
	verifyListOfLength(5);
}
