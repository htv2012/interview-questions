#ifndef LIST_H_AXCFF
#define LIST_H_AXCFF

/**
 * @file linkedlist.h
 * 
 */

#ifdef __cplusplus
extern "C" {
#endif

#include <stdlib.h>

/* === Data Structures === */
typedef struct _node {
	int data;
    struct _node *next;
} node;

#define EMPTY_NODE ((node*)NULL) 
extern const int LIST_OK;
extern const int LIST_INVALID_PARAMETER;

/* === Functions === */
void list_append(node **head, int data);
node* list_create();
int list_length(node *head);

/**
Given two lists, write a function to determine if they will eventually
merged.
*/
node* list_are_merged(node *head1, node* head2);

/**
 * Find the Nth element from a singly linked list from
 * the end in one pass.
 *  
 * @param head The pointer to the first node of the linked list
 * @param n The number of nodes from the tail to find.
 * 
 * @return the pointer to the Nth node from the tail, or EMPTY_NODE if n 
 * exceeds the list's length. If n is zero, the function will return
 * the pointer to the last node.
 */
node *list_find_nth_node_from_tail(node *head, int n);

/*
Given a list, determine if it has a loop.
*/
int list_has_loop(node *head);

/*
Similar to list_reverse(), but with a twist: given a list and a number
n, skip n nodes and reverse the rest.
*/
int list_skip_and_reverse(node **head, int n);

/*
Given an integer linked list of which both first half and second half
are sorted independently. Write a function to merge the two parts to
create one single sorted linked list in place. Do not use any extra
space.
*/
void list_merge_two_halves(node **head);

/*
Given a list, reverse it.
*/
void list_reverse(node **head);


/*
Given a list and an integer `n`, swap the two nodes nth node from
the beginning and nth node from the end of the list.
*/
int list_swap_nodes(node* head, int n);

#ifdef __cplusplus
}
#endif
#endif // LIST_H_AXCFF

