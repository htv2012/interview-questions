/**
 * @file: std_list.cpp
 * 
 * A test drive of std::list type and its iterator
 */

#include <iostream>
#include <list>
using namespace std;

int main(int argc, char **argv) {
    int ar[] = {9, 18, 27, 36, 45};
    list<int> ls(ar, ar + 5);

    cout << "List:";
    for (list<int>::iterator it = ls.begin(); it != ls.end(); ++it) {
        cout << " " << *it;
    }
    cout << endl;
    return 0;
}

