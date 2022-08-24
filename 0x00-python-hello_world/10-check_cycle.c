#include "lists.h"

/**
 * check_cycle - checks for cycle in list
 * @list: points to head of cycle
 * Return: 1 if present 0 if none
 */
int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	slow = fast = list;
	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
		{
			return (1);
		}
	}
	return (0);
}
