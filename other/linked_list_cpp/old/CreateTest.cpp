#include "common.h"

TEST(ListConstructorTest, CheckSize) {
    List list;
    ASSERT_EQ(0U, list.size());
}
TEST(ListConstructorTest, CheckEmpty) {
    List list;
    ASSERT_TRUE(list.empty());
}
