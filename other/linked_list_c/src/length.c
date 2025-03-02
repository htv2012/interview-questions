#include "linkedlist.h"

int list_length(node *head) {
	int length = 0;
	node *current;
	for (current = head; current; current = current->next) {
		++length;
	}
	return length;
}


