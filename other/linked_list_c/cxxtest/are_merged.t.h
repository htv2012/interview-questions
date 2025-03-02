#include "common.h"

class AreMergedSuite: public CxxTest::TestSuite, ListTest {
public:
    void testOneEmptyList() {
        list1 = createListOfLength(5);
        TS_ASSERT_EQUALS(EMPTY_NODE, list_are_merged(list1, list2));
        TS_ASSERT_EQUALS(EMPTY_NODE, list_are_merged(list2, list1));
    }

    void testTwoEmptyList() {
        TS_ASSERT_EQUALS(EMPTY_NODE, list_are_merged(list1, list2));
    }

    void testNotMerged() {
        list1 = createListOfLength(5);
        list2 = createListOfLength(8);
        TS_ASSERT_EQUALS(EMPTY_NODE, list_are_merged(list1, list2));
    }

    void testSameList() {
        list1 = createListOfLength(1);
        TS_ASSERT_EQUALS(list1, list_are_merged(list1, list1));
    }

    // list1 -> 0-> 1 -> 2 -> 3 -> 4 
    // list2 -> 0 -------^
    void testMergeAtMiddle() {

    }

    void setUp() {
        list1 = list_create(); 
        list2 = list_create(); 
    }

    void tearDown() {
        clearList(&list1);
        clearList(&list2);
    }

    // void createMergedLists(length1, length2, mergedNodeNumber) {
    //     list1 = createListOfLength(length1);
    //     list2 = createListOfLength(length2);

    //     node* list2;
    //     node* p;
    //     int i;
        
    //     for (last2 = list2; last2->next; last2 = last2->next)
    //         ;
    //     for (i = 0, p = list1; i < mergedNodeNumber; i++, p = p->next)
    //         ;
    //     last2->next = p;
    //     mergedNode = p;
    // }

private:
    node* list1;
    node* list2;
    node* mergedNode;
};
