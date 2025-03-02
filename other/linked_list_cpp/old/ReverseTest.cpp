#include "common.h"

/**********************************************************************
 * Test fixture
 */

class ReverseTest: 
		public ::testing::TestWithParam< unsigned int > {
public:
	void setUp() {list = NULL; }
	void tearDown() { delete list; }

	void verifyListOfLength(unsigned int n, bool reversed=false) {
		List::iterator it;
		int i;
		for (i = 0, it = list->begin();
				i < n;
				i++, it++) {
			EXPECT_TRUE(it != list->end())
				<< "List is missing node(s)";
			EXPECT_EQ(reversed ? n - i - 1 : i, *it)
				<< "Node value is not what expected";
		}

		ASSERT_TRUE(it == list->end()) 
			<< "List has extra node(s)";
	}

	void performReverseOnceTest(unsigned int numberOfNodes) {
		list = createListOfLength(numberOfNodes);
		list->reverse();
		verifyListOfLength(numberOfNodes, true);
	}

	void performReverseTwiceTest(unsigned int numberOfNodes) {
		performReverseOnceTest(numberOfNodes);
		list->reverse();
		verifyListOfLength(numberOfNodes);
	}
protected:
	List* list;
};

/**********************************************************************
 * Tests
 */


TEST_P(ReverseTest, reverseOnce) {
	unsigned int numberOfNodes = (unsigned int)GetParam();
	performReverseOnceTest(numberOfNodes);
}

TEST_P(ReverseTest, reverseTwice) {
	unsigned int numberOfNodes = (unsigned int)GetParam();
	performReverseTwiceTest(numberOfNodes);
}

INSTANTIATE_TEST_CASE_P(
	GeneralCases,
    ReverseTest,
    ::testing::Range(3U, 20U));

INSTANTIATE_TEST_CASE_P(
	CornerCases,
    ReverseTest,
    ::testing::Values(0U, 1U, 2U, 999U, 1000U));

