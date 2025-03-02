#include "common.h"

/**********************************************************************
 * Test fixture
 */

class MergeTwoHalvesTest : public ListTest {
public:
    node *createFromArray(int ar[], int count) {
        node *new_list = list_create();
        int i;
        for (i = 0; i < count; i++) {
            list_append(&new_list, ar[i]);
        }
        return new_list;
    }

    void doTest(int input[], int expected[], int count) {
        list = createFromArray(input, count);
        list_merge_two_halves(&list);
        node *p;
        int i;
        for (i = 0, p = list; i < count; i++, p = p->next) {
            ASSERT_EQ(expected[i], p->data);
        }
        ASSERT_EQ(EMPTY_NODE, p);
    }

};

/**********************************************************************
 * Tests
 */

TEST_F(MergeTwoHalvesTest, EmptyList) {
    ASSERT_TRUE(list == EMPTY_NODE);
    list_merge_two_halves(&list);
    ASSERT_TRUE(list == EMPTY_NODE);
}
TEST_F(MergeTwoHalvesTest, OneNode) {
    list = createListOfLength(1);
    list_merge_two_halves(&list);
    EXPECT_NE(EMPTY_NODE, list);
    EXPECT_EQ(0, list->data);
}
TEST_F(MergeTwoHalvesTest, TwoNodesSorted) {
    int ar[] = {2, 9};
    list = createFromArray(ar, 2);
    list_merge_two_halves(&list);

    EXPECT_NE(EMPTY_NODE, list);
    EXPECT_EQ(2, list->data);
    EXPECT_EQ(9, list->next->data);
}
TEST_F(MergeTwoHalvesTest, TwoNodesUnsorted) {
    int ar[] = {19, 9};
    list = createFromArray(ar, 2);
    EXPECT_EQ(19, list->data);
    EXPECT_EQ(9, list->next->data);
    list_merge_two_halves(&list);

    EXPECT_NE(EMPTY_NODE, list);
    EXPECT_EQ(9, list->data);
    EXPECT_EQ(19, list->next->data);
}
TEST_F(MergeTwoHalvesTest, ThreeNodesSorted) {
    int input[] = {1, 2, 3};
    int expected[] = {1, 2, 3};
    doTest(input, expected, 3);
}
TEST_F(MergeTwoHalvesTest, ThreeNodesCase2) {
    int input[] = {1, 3, 2};
    int expected[] = {1, 2, 3};
    doTest(input, expected, 3);
}
TEST_F(MergeTwoHalvesTest, ThreeNodesCase3) {
    int input[] = {2, 1, 3};
    int expected[] = {1, 2, 3};
    doTest(input, expected, 3);
}
TEST_F(MergeTwoHalvesTest, ListOneEndsFirst) {
    int input[] = {2, 4, 1, 5, 6};
    int expected[] = {1, 2, 4, 5, 6};
    int count = sizeof(input) / sizeof(int);
    doTest(input, expected, count);
}
TEST_F(MergeTwoHalvesTest, ListTwoEndsFirst) {
    int input[] = {2, 7, 1, 5, 6};
    int expected[] = {1, 2, 5, 6, 7};
    int count = sizeof(input) / sizeof(int);
    doTest(input, expected, count);
}
TEST_F(MergeTwoHalvesTest, ListsOfSameLength) {
    int input[] = {2, 4, 6, 1, 3, 5};
    int expected[] = {1, 2, 3, 4, 5, 6};
    int count = sizeof(input) / sizeof(int);
    doTest(input, expected, count);
}
TEST_F(MergeTwoHalvesTest, ListOneHasOneElement) {
    int input[] = {30, 10, 20, 40, 50, 60};
    int expected[] = {10, 20, 30, 40, 50, 60};
    int count = sizeof(input) / sizeof(int);
    doTest(input, expected, count);
}
TEST_F(MergeTwoHalvesTest, ListTwoHasOneElement) {
    int input[] = {10, 20, 40, 50, 60, 30};
    int expected[] = {10, 20, 30, 40, 50, 60};
    int count = sizeof(input) / sizeof(int);
    doTest(input, expected, count);
}

