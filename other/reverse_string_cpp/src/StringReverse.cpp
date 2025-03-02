#include "StringReverse.h"
#include <iostream>
using namespace std;

void StringReverse(char* str) {
    if (!str || !*str) return;

    char* left = str;
    char* right = str;
    char temp;

    for (; *right; ++right)
        ;
    --right;
    
    for (; left < right; ++left, --right) {
        temp = *left;
        *left = *right;
        *right = temp;
    }

}