# Project setup
project(linked_list_cpp)
cmake_minimum_required(VERSION 2.8.12)
include_directories(${CMAKE_CURRENT_SOURCE_DIR}/src)
add_compile_options(-std=c++14 -stdlib=libc++)

# Library, or system under test
aux_source_directory(src LIB_SOURCES)
add_library(linkedlist ${LIB_SOURCES})

# Test
enable_testing(true)
aux_source_directory(tests TEST_SOURCES)
add_executable(linked_list_tests ${TEST_SOURCES})
target_link_libraries(linked_list_tests linkedlist)
add_test(linked_list_tests linked_list_tests)
