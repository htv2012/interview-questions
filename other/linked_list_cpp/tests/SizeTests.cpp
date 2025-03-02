#include <catch.hpp>
#include <LinkedList.h>

TEST_CASE("Size Tests") {
    LinkedList<int> list;

    SECTION("New List has size 0") { REQUIRE(0 == list.size()); }
    SECTION("New list's head is nullptr") { REQUIRE(nullptr == list.get_head()); }
    SECTION("New list's tail is nullptr") { REQUIRE(nullptr == list.get_tail()); }

    const int element = 1950;
    list.push_back(element);

    SECTION("Push first item, check size") { REQUIRE(1 == list.size()); }
    SECTION("Push first item, check head") {
        REQUIRE(nullptr != list.get_head());
        REQUIRE(element == list.get_head()->data);
    }
    SECTION("Push first item, check tail") {
        REQUIRE(nullptr != list.get_tail());
        REQUIRE(element == list.get_tail()->data);
    }
}

