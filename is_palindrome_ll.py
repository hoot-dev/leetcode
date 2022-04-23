
"""
Problem:
Given the head of a singly linked list, return true if it is a palindrome.
"""

def is_palindrome(self, head):
    # problem, we have no idea how long this thing is
    # if we know the half way point we could store a mapping
    # of value and its location in the linked list and check that
    # mapping as we come down the back side, as soon as we find
    # a non-match we can return false
    
    # a solution (not optimal):
    # just create a list as you traverse the linked list
    # at the end compare list[::-1] to list and we are done
    
    values = []
    current = head
    while True:
        values.append(current.val)
        if current.next:
            current = current.next
        else:
            break
    return values == values[::-1]


def isPalindrome(self, head):
    # rev records the first half, need to set the same structure as fast, slow, hence later we have rev.next
    rev = None
    # initially slow and fast are the same, starting from head
    slow = fast = head
    while fast and fast.next:
        # fast traverses faster and moves to the end of the list if the length is odd
        fast = fast.next.next
        
        # take it as a tuple being assigned (rev, rev.next, slow) = (slow, rev, slow.next), hence the re-assignment of slow would not affect rev (rev = slow)
        rev, rev.next, slow = slow, rev, slow.next
    if fast:
       # fast is at the end, move slow one step further for comparison(cross middle one)
        slow = slow.next
    # compare the reversed first half with the second half
    while rev and rev.val == slow.val:
        slow = slow.next
        rev = rev.next
    
    # if equivalent then rev become None, return True; otherwise return False 
    return not rev

    """
    What the heck is this thing doing?
    Using multiple iterators at the same time to iterate the list fast and slow
    The "fast" iterator goes double speed through the list
        - fast = fast.next.next
    The "slow" iterator goes one at a time and is used to create a reversed 
    linked list of the front half called "rev"
        - rev, rev.next, slow = slow, rev, slow.next
    Once fast hits the end we check if fast is None or not
        if fast is not none then we move slow up one more as this linked list length is an odd 
        number so the mid point is actually "between" two links
        this ensures that slow is starting at the second half of the list and we don't care about
        the middle link because if it's even in length the mid has no mirror link to compare
    now we just iterate over the reversed first half while slow keeps chugging along over the back
    half
        if we ever hit a point where rev.val != slow.val we break out of the loop
        if we broke out of the loop early that means there is still at least one link in reverse list
        so reverse list will be true as it has value
        if we made it to the end of reverse then reverse is None
    return "not rev"
    """