#include <stdarg.h>
#include <stddef.h>
#include <setjmp.h>
#include <cmocka.h>
#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

#define BUFFER_SIZE 1024

void do_test(long long_value) {
    char expected_value[BUFFER_SIZE];
    char actual_value[BUFFER_SIZE];
    char cmd[1024];

    // Create expected value
    sprintf(expected_value, "%ld", long_value);
    printf("Expect: >%ld<\n", long_value);

    // TODO: not to hard code file's location
    sprintf(cmd, "./putlong_runner %ld", long_value);
    FILE* pipe = popen(cmd, "r");

    // TODO: Check for pipe open failed

    fgets(actual_value, BUFFER_SIZE-1, pipe);
    printf("Actual: >%s<\n", actual_value);

    // Verify
    assert_string_equal(expected_value, actual_value);

}

static void test_one()                           { do_test(1L); }
static void test_negative_one()                  { do_test(-1L); }
static void test_zero()                          { do_test(0L); }
static void test_zero_ending()                   { do_test(19700L); }
static void test_negative_with_zero_ending()     { do_test(-19700L); }
static void test_long_max()                      { do_test(LONG_MAX); }
static void test_near_long_max()                 { do_test(LONG_MAX - 1); }
static void test_near_long_max_with_zero_ending(){ do_test(LONG_MAX / 10 * 10); }
static void test_long_min()                      { do_test(LONG_MIN); }
static void test_near_long_min()                 { do_test(LONG_MIN + 1); }
static void test_embedded_zero()                 { do_test(9208L); }

int main(void) {
    const UnitTest tests[] = {
        unit_test(test_one),
        unit_test(test_negative_one),
        unit_test(test_zero),
        unit_test(test_zero_ending),
        unit_test(test_negative_with_zero_ending),
        unit_test(test_long_max),
        unit_test(test_long_min),
        unit_test(test_near_long_max),
        unit_test(test_near_long_max_with_zero_ending),
        unit_test(test_near_long_min),
        unit_test(test_embedded_zero),
    };

    return run_tests(tests);
}
