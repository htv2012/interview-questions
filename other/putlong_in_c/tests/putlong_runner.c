/* 
 * This is a driver, used by cmocka_test.c.  
 */

#include <stdio.h>
#include <stdlib.h>
#include "putlong.h"

int main(int argc, char const *argv[]) {
    char *error_found;
    long long_value = strtol(argv[1], &error_found, 10);
    putlong(long_value);
    fflush(stdout);
    return EXIT_SUCCESS;
}