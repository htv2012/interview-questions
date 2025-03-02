#include <stdio.h>
#include <limits.h>

void putlong(long number) {
    char digit;
    long extractor = (number > 0 ? 1 : (number <= -10 ? -10 : -1));
    for (; number / extractor >= 10; extractor *= 10)
        ;
    if (number < 0) putchar('-');
    
    while (number != 0) {
        digit = (char)(number / extractor + '0');
        putchar(digit);
        number %= extractor;
        extractor /= 10;
    }
    for (; extractor != 0; extractor /= 10)
        putchar('0');
}
