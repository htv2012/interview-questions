// try out: putlong()

#include <stdio.h>
#include <stdlib.h>
#include <limits.h>
#include "putlong.h"

int main(int argc, char const *argv[]) {
    long test_cases[] = {LONG_MAX, LONG_MIN, -1, 0, 1};
    int test_count = sizeof(test_cases) / sizeof(test_cases[0]);
    int i;

    for (i = 0; i < test_count; i++) {
        printf(">%ld<\n", test_cases[i]);
        putchar('>');
        putlong(test_cases[i]);
        printf("<\n\n");
    }

    return 0;
}