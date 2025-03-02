#include "common.h"

// CreateTest.cpp
// Test list_create()

TEST(CreateTest,expect_null) {
    ASSERT_EQ(EMPTY_NODE, list_create());
}

