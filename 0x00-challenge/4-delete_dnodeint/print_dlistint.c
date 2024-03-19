#include <stdio.h>
#include "lists.h"

/**
 * Outputs the elements of a doubly linked list of integers.
 * @h: A pointer to the head of the list.
 * Return: The count of elements printed.
 */
size_t print_dlistint(const dlistint_t *h)
{
    size_t count;

    count = 0;
    while (h)
    {
        printf("%d\n", h->n);
        h = h->next;
        count++;
    }
    return (count);
}

