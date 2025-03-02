#include "linkedlist.h"

int list_skip_and_reverse(node **head, int n) {
	// Skip n nodes
	node *tail = EMPTY_NODE;
	node *current = *head;
	while (n--) {
		if (!current) return LIST_INVALID_PARAMETER;
		tail = current;
		current = current->next;
	}

	// Reverse the rest
	node *previous = EMPTY_NODE;
	node *next;
	while (current) {
		next = current->next;
		current->next = previous;
		previous = current;
		current = next;
	}

	// Fix up the tail. If n was 0, then fix up the head
	if (tail) {
		tail->next = previous;
	} else {
		*head = previous;
	}
	return LIST_OK;
}
