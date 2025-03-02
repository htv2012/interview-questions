#include <vector>

#define CATCH_CONFIG_MAIN
#include <catch.hpp>

#include "odd_even_arrangement.h"


void validate_odd_even(const std::vector<int>& vec) {
    for (int i = 0; i < vec.size(); i++) {
        CAPTURE(i);
        CAPTURE(vec[i]);
        REQUIRE(isodd(i) == isodd(vec[i]));
    }
}

TEST_CASE("Test case 1", "[odd_even]") {
    std::vector<int> vec {1, 2, 3, 4};
    arrange_odd_even(vec);
    validate_odd_even(vec);
}

TEST_CASE("Test empty", "[odd_even") {
    std::vector<int> v;
    arrange_odd_even(v);
    validate_odd_even(v);
}

TEST_CASE("Test no swap", "[odd_even]") {
    std::vector<int> v {2, 5, 4, 7, 10, 9};
    arrange_odd_even(v);
    validate_odd_even(v);
}

TEST_CASE("Many swaps", "[odd_even]") {
    std::vector<int> v {1, 3, 5, 7, 2, 4, 6, 8};
    arrange_odd_even(v);
    validate_odd_even(v);
}

TEST_CASE("Odds are at one end", "[odd_even]") {
    std::vector<int> v {2, 4, 6, 3, 5, 7};
    arrange_odd_even(v);
    validate_odd_even(v);
}
