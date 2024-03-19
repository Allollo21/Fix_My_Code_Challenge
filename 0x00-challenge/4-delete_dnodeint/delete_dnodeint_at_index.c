#include "lists.h"
#include <stdlib.h>

/**
 * Removes a node from a specified index in a doubly linked list.
 * @head: A pointer to the head of the list.
 * @index: The index from which the node should be removed.
 * Return: 1 if successful, -1 if an error occurs.
 */
int delete_dnodeint_at_index(dlistint_t **head, unsigned int index)
{
    dlistint_t *current_head;
    dlistint_t *node_to_delete;
    unsigned int current_index;

    if (*head == NULL)
    {
        return (-1);
    }
    current_head = *head;
    current_index = 0;
    while (current_index < index && *head != NULL)
    {
        *head = (*head)->next;
        current_index++;
    }
    if (current_index != index)
    {
        *head = current_head;
        return (-1);
    }
    if (index == 0)
    {
        node_to_delete = (*head)->next;
        free(*head);
        *head = node_to_delete;
        if (node_to_delete != NULL)
        {
            node_to_delete->prev = NULL;
        }
    }
    else
    {
        node_to_delete = *head;
        node_to_delete->prev->next = node_to_delete->next;
        if (node_to_delete->next)
        {
            node_to_delete->next->prev = node_to_delete->prev;
        }
        free(node_to_delete);
        *head = current_head;
    }
    return (1);
}

