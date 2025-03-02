#include "common.h"

class PushBackTest: public testing::Test {
public:

    void push_back_and_get_iterator(int item) {
        list.push_back(item);
        it = list.begin();
    }
    void push_back_two_items(int item1, int item2) {
        list.push_back(item1);
        list.push_back(item2);
        it = list.begin();
    }

    void push_back_many_and_verify(int items[], int count) {
        int i;

        // Push and verify the size
        for (i = 0; i < count; i++) {
            list.push_back(items[i]);
            ASSERT_EQ(i + 1, list.size());
        }

        // Verify the items are pushed in order
        for (i = 0, it = list.begin();
                it != list.end();
                i++, it++) {
            ASSERT_EQ(items[i], *it);
        }

        // Verify the emptiness
        ASSERT_FALSE(list.empty());
    }

    List list;
    List::iterator it;
};

TEST_F(PushBackTest, PushOneItemCheckData) {
    push_back_and_get_iterator(5);
    ASSERT_EQ(5, *it);
}
TEST_F(PushBackTest, PushOneItemCheckSize) {
    push_back_and_get_iterator(5);
    ASSERT_EQ(1, list.size());
}
TEST_F(PushBackTest, PushOneItemCheckNotEmpty) {
    push_back_and_get_iterator(5);
    ASSERT_FALSE(list.empty());
}

TEST_F(PushBackTest, PushTwoItemsCheckData) {
    push_back_two_items(5, -80);
    ASSERT_EQ(5, *it);
    ++it;
    ASSERT_EQ(-80, *it);
}
TEST_F(PushBackTest, PushTwoItemsCheckSize) {
    push_back_two_items(-9, 1);
    ASSERT_EQ(2, list.size());
}
TEST_F(PushBackTest, PushTwoItemsCheckNotEmpty) {
    push_back_two_items(9, -10);
    ASSERT_FALSE(list.empty());
}

TEST_F(PushBackTest, PushEightItems) {
    int items[] = {2, 3, 6, 7, 10, 11, 14, 15};
    push_back_many_and_verify(items, 8);
}
