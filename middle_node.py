"""
Problem:
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.
"""

def middleNode(head):
    slow = fast = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    return slow

"""
This is just a sub-problem of finding a palindrome in a linked list
while using the same technique to find the mid point with a fast iterator
and a slow iterator
When the fast iterator hits the end, the slow iterator is at the middle
"""