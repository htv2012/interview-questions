#include "common.h"

class StressTest : public ListTest {
protected:
    int hugeListSize;
    void readTestData() {
        // TODO: Read from a file, to allow changing in the fly
        hugeListSize = 10000;
    }


    virtual void SetUp() { ListTest::SetUp(); readTestData(); }
};

TEST_F(StressTest, create_huge_list) {
    list = createListOfLength(hugeListSize);
}

TEST_F(StressTest, append_many_times) {
    list = createListOfLength(hugeListSize);
    for (int i = 0; i < hugeListSize; i++) {
        list_append(&list, i);
        list_reverse(&list);
    }
}

