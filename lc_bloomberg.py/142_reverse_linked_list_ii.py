# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if not head: return None

        prev = None
        curr = head

        while m > 1:
            prev = curr
            curr = curr.next
            n -= 1
            m -= 1

        connection, tail = prev, curr

        while n:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
            n -= 1

        if connection is not None:
            connection.next = prev
        else:
            head = prev

        tail.next = curr

        return head


"""
    create a prev var, pointing to None
    create a curr var, pointing to head
    
    *get to the node where we want to start reversing
    while m > 1:
        move prev to curr
        move curr to curr.next
        decrement m and n
    
    save prev and curr to connection and tail variables, as we're going to use these to reconnect
    
    while n:
        create next to not lose connection to rest
        curr.next = prev to reverse
        move prev to curr
        curr to next
        dec n
        
    if connection is not None:
        connection.next = prev to connect the beginning to reversed beginning
    else:
        prev becomes head
        
    tail.next = curr to connect the end to reversed end
    
    return head
