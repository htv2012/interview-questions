#include "common.h"

class LengthSuite: public CxxTest::TestSuite, ListTest {
public:
    void testEmpty(void)   { TS_ASSERT_EQUALS(0, list_length(EMPTY_NODE)); }
    void testListOfOne()   { performCheck(1); }
    void testListOfTwo()   { performCheck(2); }
    void testListOfThree() { performCheck(3); }
    void testListOf99()    { performCheck(99); }
    void testLongList()    { performCheck(100); }

    void performCheck(int n) {
        node* list = createListOfLength(n);
        TS_ASSERT_EQUALS(n, list_length(list));
    }
};