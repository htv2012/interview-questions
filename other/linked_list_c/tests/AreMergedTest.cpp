#include "common.h"

/**********************************************************************
 * Test fixture
 */

class AreMergedTest : public ListTest {
public:
    node *list1;
    node *list2;
    void SetUp() {
        list1 = list2 = NULL;
    }
    void TearDown() {
        clearList(&list1);
        clearList(&list2);
    }
};

/**********************************************************************
 * Tests
 */

TEST_F(AreMergedTest, atLeastOneListIsEmpty_ExpectFalse) {
    EXPECT_EQ(NULL, list_are_merged(list1, list2));
    std::cout << 1 << std::endl;

    list1 = createListOfLength(1);
    std::cout << 2 << std::endl;
    EXPECT_EQ(NULL, list_are_merged(list2, list1));
    std::cout << 3 << std::endl;
    EXPECT_EQ(NULL, list_are_merged(list1, list2));
    std::cout << 4 << std::endl;
}

TEST_F(AreMergedTest, notMerged_ExpectFalse) {
    list1 = createListOfLength(5);
    list2 = createListOfLength(2);

    EXPECT_EQ(NULL, list_are_merged(list1, list2));
    EXPECT_EQ(NULL, list_are_merged(list2, list1));
}

TEST_F(AreMergedTest, sameList_ExpectTrue) {
    list1 = createListOfLength(2);
    EXPECT_EQ(list1, list_are_merged(list1, list1));
}

// list1 -> 0-> 1 -> 2 -> 3 -> 4 
// list2 -> 0 -------^
TEST_F(AreMergedTest, mergedAtMiddle_ExpectTrue) {
    list1 = createListOfLength(5);
    list2 = createListOfLength(1);
    node* intersection = list1->next->next;
    list2->next = intersection;

    EXPECT_EQ(intersection, list_are_merged(list1, list2));
    EXPECT_EQ(intersection, list_are_merged(list2, list1));
    list2->next = NULL;
}

// list1 -> 0 -> 1 -> 2
// list2 -> 0 --------^
TEST_F(AreMergedTest, mergeAtEnd_ExpectTrue) {
    list1 = createListOfLength(3);
    list2 = createListOfLength(1);
    node* intersection = list1->next->next;
    list2->next = intersection;

    EXPECT_EQ(intersection, list_are_merged(list1, list2));
    EXPECT_EQ(intersection, list_are_merged(list2, list1));
    list2->next = NULL;
}

// list1 -> 0 -> 1 -> 2 -> 4
// list2 --------^
TEST_F(AreMergedTest, subList_ExpectTrue) {
    list1 = createListOfLength(5);
    node* intersection = list1->next;
    list2 = intersection;

    EXPECT_EQ(intersection, list_are_merged(list1, list2));
    EXPECT_EQ(intersection, list_are_merged(list2, list1));
    list2 = NULL;
}

/*
 * list1 -> 0 -> 1 -> 2 -> 3 ->4
 * list2 -> 0 -> 1 -> 2 ---^
 */
TEST_F(AreMergedTest, mergeNearEnd_ExpectTrue) {
    list1 = createListOfLength(5);
    list2 = createListOfLength(3);
    node* intersection = list1->next->next->next;
    list2->next->next->next = intersection;

    EXPECT_EQ(intersection, list_are_merged(list1, list2));
    EXPECT_EQ(intersection, list_are_merged(list2, list1));
    list2->next->next->next = NULL;
}

/*
 * list1 -> 0 -> 1 -> 2 -> 3
 * list2 -> 0 -> 1 ---^
 */
TEST_F(AreMergedTest, listOfSameLength_expecTrue) {
    list1 = createListOfLength(4);
    list2 = createListOfLength(2);
    node* intersection = list1->next->next;
    list2->next->next = intersection;

    EXPECT_EQ(intersection, list_are_merged(list1, list2));
    EXPECT_EQ(intersection, list_are_merged(list2, list1));

    list2->next->next = EMPTY_NODE;
}

/*
 * list1 -> 0 -> 1 -> 2 -> 3 -> 4
 * list2 -> 0 -> 1 -> 2 -> 3 -> 4
 */
TEST_F(AreMergedTest, listOfSameLength_expecFalse) {
    list1 = createListOfLength(4);
    list2 = createListOfLength(4);
    EXPECT_EQ(NULL, list_are_merged(list1, list2));
    EXPECT_EQ(NULL, list_are_merged(list2, list1));
}
