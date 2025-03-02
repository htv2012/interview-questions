#include "common.h"

class AppendSuite: public CxxTest::TestSuite, ListTest {
public:
    void testAppend1()  { performCheck(1); }
    void testAppend2()  { performCheck(2); }
    void testAppend3()  { performCheck(3); }
    void testAppend99() { performCheck(99); }

    void performCheck(int n) {
        for (int i = 0; i < n; i++) {
            list_append(&list, i);
        }
        node* p = list;
        for (int i = 0; i < n; i++) {
            TS_ASSERT_EQUALS(i, p->data);
            p = p->next;
        }
    }

    void setUp()    { list = list_create(); }
    void tearDown() { clearList(&list); }

private:
    node* list;
};