project(interview)
cmake_minimum_required(VERSION 2.8.12)

# Options
add_compile_options(-std=c++14 -stdlib=libc++)
enable_testing(true)
include_directories(${CMAKE_HOME_DIRECTORY}/external/catch)

# Sub projects
add_subdirectory(odd_even_arrangement_cpp)
add_subdirectory(linked_list_cpp)

