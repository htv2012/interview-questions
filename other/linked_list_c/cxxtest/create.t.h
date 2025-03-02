#include <cxxtest/TestSuite.h>
#include "linkedlist.h"
class CreateSuite: public CxxTest::TestSuite {
public:
    void testCreate(void) {
        TS_ASSERT_EQUALS(EMPTY_NODE, list_create());
    }
};