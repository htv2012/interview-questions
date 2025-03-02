#include "SqueezeSpaces.h"
#include <iostream>
using namespace std;

const char SPACE = ' ';

void SqueezeSpaces(char* str) {
    if (!str || !*str) return;
    cout << "str = " << &str << endl;
    cout << "Original >>> " << str << "<<<" << endl;
    char *dest = str;
    char *src = str;

    // Skip initial spaces
    // for (src = str; *src && *src == SPACE; ++src)
    //     cout << "skip >>>>>>" << *src << "<<<" << endl;
    // cout << "First char: " << src <<  " " << &src << endl;

    // Copy loop
    while (*src) {
        // skip spaces
        for (; *src && *src == SPACE; ++src)
            cout << "skip space" << endl;

        // copy until space
        for (; *src && *src != SPACE; ++dest, ++src) {
            *dest = *src;
            cout << "Copy >" << *src << endl;
        }

        // Copy one space
        *dest++ = *src++;
        cout <<"copy space\n" ;

    }

    cout << "Dest: " << *dest << endl;
    // Terminate the string
    if (*dest == SPACE) --dest;
    *dest = '\0';

    cout << "After, str = >" << str << "<" << endl;
}
