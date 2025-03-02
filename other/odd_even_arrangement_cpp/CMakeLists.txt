# Options
cmake_minimum_required(VERSION 2.8.12)
project(odd_even_arrangement)

# Library, or system under test
add_library(odd_even_arrangement odd_even_arrangement.cpp)

# Test executable
add_test(odd_even_arrangement_tests odd_even_arrangement_tests)
add_executable(odd_even_arrangement_tests odd_even_arrangement_tests.cpp)
target_link_libraries(odd_even_arrangement_tests odd_even_arrangement)
