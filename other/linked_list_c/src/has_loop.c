#include "linkedlist.h"

int list_has_loop(node *head) {
	node *faster = head;
	node *slower = head;
	int steps = 0;

	while (faster) {
		faster = faster->next;
		if (++steps % 2 == 0) slower = slower->next;
		if (faster == slower) return 1;
	}

	return 0;
}
