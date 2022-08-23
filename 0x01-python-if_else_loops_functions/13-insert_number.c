#include "lists.h"

/**
 * insert_node - inserts number in sorted linked
 * list
 * @head: points to pointer of head
 * @number: to be inserted in list
 * Return: pointer to inserted node
 * NULL on failure
 */
listint_t *insert_node(listsint_t **head, int number)
{
	listint_t *node = *head, *new_node;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	new_node->n = number;
	if (node == NULL || node->n >= number)
	{
		new_node->next = node;
		*head = new_node;
		return (new_node);
	}
	while (node && node->next && node->next->n < number)
		node = node->next;
	new_node->next = node->next;
	node->next = new_node;
	return (new_node);
}
