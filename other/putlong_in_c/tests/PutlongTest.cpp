/***********************************************************************
* HEADER
***********************************************************************/

#include <iostream>
#include <climits>
#include <gtest/gtest.h>
#include "putlong.h"
#include <string>
#include <sstream>
#include <stdio.h>

#if defined _WIN32 || defined _WIN64
#include <conio.h>
#define popen _popen
#define pclose _pclose
#define PUTLONG_RUNNER "putlong_runner"
#else
#define PUTLONG_RUNNER "./putlong_runner"
#endif

using namespace std;

class PutlongTest : public testing::TestWithParam<long> {
public:
    virtual void SetUp();
protected:
    long numberToBeTested;
    string expectedValue;
    string actualValue;
    string getPutlongOutput();
};

/***********************************************************************
* TEST
***********************************************************************/

TEST_P(PutlongTest, putlong_test) {
    actualValue = getPutlongOutput();
    ASSERT_EQ(expectedValue, actualValue);
}

/***********************************************************************
* TEST PARAMETERS
***********************************************************************/

INSTANTIATE_TEST_CASE_P(
    NormalCases, 
    PutlongTest, 
    testing::Values(125, -17, -2345678, 56789));

INSTANTIATE_TEST_CASE_P(
    NumbersWithZeroTestCases,
    PutlongTest,
    testing::Values(
        10, 200, 3000, 40000, 500000,
        809, 90000003, 300700));

INSTANTIATE_TEST_CASE_P(
    CornerCases,
    PutlongTest,
    testing::Values(    
        LONG_MAX, LONG_MAX-1, LONG_MAX / 10 * 10,
        LONG_MIN, LONG_MIN + 1, LONG_MIN / 10 * 10,
        0, -1, 1));

/***********************************************************************
* TEST FIXTURES & SUPPORT
***********************************************************************/

void PutlongTest::SetUp() {
    numberToBeTested = (long)GetParam();

    // Create expected value
    ostringstream buffer;
    buffer << numberToBeTested;
    expectedValue = buffer.str();
}

string PutlongTest::getPutlongOutput() {
    // Create command line for communication with putlong_runner
    ostringstream buffer;
    buffer << PUTLONG_RUNNER << " " << numberToBeTested;
    string pipe_command = buffer.str();

    // Create a communication channel with putlong_runner and get
    // back the long number printed by putlong()
    const int BUFFER_SIZE = 1024;
    FILE* pipe = popen(pipe_command.c_str(), "r");
    
    char putlong_output[BUFFER_SIZE];
    fgets(putlong_output, BUFFER_SIZE-1, pipe);
    string output = putlong_output;
    pclose(pipe);
    return output;
}

