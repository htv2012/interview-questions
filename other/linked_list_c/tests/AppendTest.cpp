#include "common.h"

class AppendTest : public ListTest {
};

TEST_F(AppendTest, append_one_node) {
	const int CHECK_VALUE = -19;
	list_append(&list, CHECK_VALUE);
	
	ASSERT_NE(EMPTY_NODE, list);
	EXPECT_EQ(CHECK_VALUE, list->data);
	EXPECT_EQ(EMPTY_NODE, list->next);
}

TEST_F(AppendTest, append_two_nodes) {
	const int CHECK_VALUE1 = 95;
	const int CHECK_VALUE2 = -7;
	list_append(&list, CHECK_VALUE1);
	list_append(&list, CHECK_VALUE2);
	
	ASSERT_NE(EMPTY_NODE, list);
	ASSERT_NE(EMPTY_NODE, list->next);
	ASSERT_EQ(EMPTY_NODE, list->next->next);
	
	EXPECT_EQ(CHECK_VALUE1, list->data);
	EXPECT_EQ(CHECK_VALUE2, list->next->data);
}

TEST_F(AppendTest, append_three_nodes) {
	const int CHECK_VALUE1 = 95;
	const int CHECK_VALUE2 = -7;
	const int CHECK_VALUE3 = 7952;
	list_append(&list, CHECK_VALUE1);
	list_append(&list, CHECK_VALUE2);
	list_append(&list, CHECK_VALUE3);
	
	ASSERT_NE(EMPTY_NODE, list);
	ASSERT_NE(EMPTY_NODE, list->next);
	ASSERT_NE(EMPTY_NODE, list->next->next);
	ASSERT_EQ(EMPTY_NODE, list->next->next->next);
	
	EXPECT_EQ(CHECK_VALUE1, list->data);
	EXPECT_EQ(CHECK_VALUE2, list->next->data);
	EXPECT_EQ(CHECK_VALUE3, list->next->next->data);
}	
