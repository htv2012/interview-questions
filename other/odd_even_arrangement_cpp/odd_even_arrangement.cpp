#include "odd_even_arrangement.h"

void arrange_odd_even(std::vector<int> &vec) {
    int even = 0;
    int odd = 1;
    auto length = vec.size();

    while (true) {
        while (even < length && !isodd(vec[even]))
            even += 2;
        while (odd < length && isodd(vec[odd]))
            odd += 2;

        if (even >= length || odd >= length)
            break;

        auto temp = vec[odd];
        vec[odd] = vec[even];
        vec[even] = temp;
    }
}

int isodd(int number) {
    return number % 2;
}
