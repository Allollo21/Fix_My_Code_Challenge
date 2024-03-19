#include <string.h>
#include <stdlib.h>
#include "lists.h"

/**
 * Deallocates the memory used by a doubly linked list.
 * @head: A pointer to the head of the list.
 */
void free_dlistint(dlistint_t *head)
{
    dlistint_t *current_node;

    while (head)
    {
        current_node = head;
        head = head->next;
        free(current_node);
    }
}

