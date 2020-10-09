class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next:
            return False

        fast = head.next
        slow = head

        while fast != slow:
            if not fast.next or not fast.next.next:
                return False
            fast = fast.next.next
            slow = slow.next

        return True

"""
    Pseudocode:
    instantiate fast and slow var (hare and tortoise), fast will start 1 node after head and slow will start at head
    create a loop to check if there is a cycle - if slow and fast meet at one point in the loop, it means there's a cycle. if fast.next and fast.next.next doesn't exist, we've run out of room and therefore there is no loop.
    edgecase - if there's no head, or head.next, return false.
"""


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        #edge case: no list at all or one node in list
        if not head:
            return False
        #instantiate two vars, fast and slow
        fast, slow = head.next, head

        #loop to see if there's a cycle.
        while slow != fast:
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next
        return True


"""
    create two pointers, fast starting at 1 node ahead of head, and slow at head
    create a loop to go on until slow is at the same node as fast (meaning there is a cycle)
        create a condition if there's no fast or fast.next, that means there's no loop. return false
        keep moving fast by 2 nodes and slow by 1 node
    if we are out of the loop, return true because fast has lapped slow
    
    Time - O(N) N = input size b/c we're looping through the entirety of the linked list
    Space - O(1) b/c we're using two pointers and not creating DS to solve the problem
"""
