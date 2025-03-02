#include "linkedlist.h"

node* list_are_merged(node* head1, node* head2) {
    int len1;
    int len2;
    node* p1;
    node* p2;

    /* find the two lengths */
    for (len1 = 0, p1 = head1; p1; ++len1, p1 = p1->next)
        ;
    for (len2 = 0, p2 = head2; p2; ++len2, p2 = p2->next)
        ;
    
    /* adjust the runners to the same distant to last nodes */
    for (p1 = head1; len1 > len2; --len1) {
        p1 = p1->next;
    }
    for (p2 = head2; len2 > len1; --len2) {
        p2 = p2->next;
    }

    /* run the nodes and compare */
    while (p1) {
        if (p1 == p2) break;
        p1 = p1->next;
        p2 = p2->next;
    }

    return p1;
}

