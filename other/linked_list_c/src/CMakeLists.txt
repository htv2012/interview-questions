cmake_minimum_required(VERSION 3.3)
project(linkedlist)

set(SOURCE_FILES
        append.c
        are_merged.c
        constants.c
        find_nth_node_from_tail.c
        has_loop.c
        length.c
        linkedlist.c
        merge_two_halves.c
        reverse.c
        skip_and_reverse.c
        swap_nodes.c)

add_library(linkedlist ${SOURCE_FILES})