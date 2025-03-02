#include "common.h"
using namespace std;

/**********************************************************************
 * Test fixture
 */

class SkipAndReverseTest : public ListTest {
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
	
	void doTest(int listLength, int n) {
		list = createListOfLength(listLength);
        list_skip_and_reverse(&list, n);
		int counter;
		int expected;
		node *p = list;
		
		// Verify the skipped-over segment of the list
		for (counter = 0; counter < n; counter++) {
			cout << "counter:" << counter << ", data:" << p->data << endl;
			EXPECT_EQ(counter, p->data);
			p = p->next;
		}
		
		// Verify the reversed segment of the list
		for (expected=listLength-1; p; counter++, expected--) {
			//cout << "counter:" << counter << ", data:" << p->data << endl;
			cout << "expected:" << expected << ", data:" << p->data << endl;
			EXPECT_EQ(expected, p->data);
			p = p->next;
		}
		
		// Make sure that the length of the list is unchanged
		cout << "n:" << n << "expected:" << expected << endl;
		EXPECT_EQ(listLength, counter);
	}
};

/**********************************************************************
 * Tests
 */

TEST_F(SkipAndReverseTest, reverseEmptyList) {
	list_skip_and_reverse(&list, 0);
	ASSERT_EQ(EMPTY_NODE, list);
	
	list_skip_and_reverse(&list, 5);
	ASSERT_EQ(EMPTY_NODE, list);	
}

TEST_F(SkipAndReverseTest, case1) {
	doTest(5, 2);	
}

TEST_F(SkipAndReverseTest, case2) {
	doTest(5, 3);	
}

TEST_F(SkipAndReverseTest, skip1) {
	doTest(5,1);
}

TEST_F(SkipAndReverseTest, skip0) {
	doTest(5,0);
}

TEST_F(SkipAndReverseTest, skipLenMinus1) {
	doTest(5,4);
}

TEST_F(SkipAndReverseTest, skipLen) {
	doTest(5,5);
}

TEST_F(SkipAndReverseTest, SkipNegativeNumber) {
	list = createListOfLength(5);
	int result = list_skip_and_reverse(&list, -1);
	ASSERT_EQ(LIST_INVALID_PARAMETER, result);
}

TEST_F(SkipAndReverseTest, lengthOf1_skip0) {
	doTest(1, 0);
}

TEST_F(SkipAndReverseTest, lengthOf1_skip1) {
	doTest(1, 1);
}

TEST_F(SkipAndReverseTest, lengthOf1_skip2) {
    list = createListOfLength(1);
    int result = list_skip_and_reverse(&list, 2);
    ASSERT_EQ(LIST_INVALID_PARAMETER, result);
}


TEST_F(SkipAndReverseTest, lengthOf1_skipNegative) {
	doTest(1, -1);
}

