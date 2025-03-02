#include "List.h"
#include <iostream>
using namespace std;

int main(int argc, char **argv)
{
    List list;

    list.push_back(3);
    list.push_back(5);
    list.push_back(7);

    cout << "List: ";
    for (List::iterator it = list.begin(); it != list.end(); it++) {
        cout << *it << " ";
    }
    cout << endl;

    return 0;
}

