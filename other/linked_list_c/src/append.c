#include "linkedlist.h"

node *create_node(int data) {
	node *new_node = (node *)malloc(sizeof(node));
	new_node->data = data;
	new_node->next = EMPTY_NODE;
	return new_node;
}


void list_append(node **head, int data) {
	node *new_node = create_node(data);
	
	if (*head) {
		node *current;
		for (current = *head; current->next; current = current->next)
			;
		current->next = new_node;
	} else {
		*head = new_node;
	}
}

