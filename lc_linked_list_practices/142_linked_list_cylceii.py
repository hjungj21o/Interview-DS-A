class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head or not head.next or not head.next.next:
            return None
        fast = head.next.next
        slow = head.next

        while fast != slow:
            if not fast or not fast.next:
                return None
            fast = fast.next.next
            slow = slow.next
            # print(fast.val, slow.val)

        fast = head

        while fast != slow:
            fast = fast.next
            slow = slow.next
        return slow


"""
    Pseudocode:
    instantiate fast and slow (hare and tortoise), fast starting at 1 node after head and slow starting at head
    create a loop to see if slow and fast meet up - if it does, it means there's a loop. if not, return None.
    set fast back to head
    create a loop to get a meetup point (this is where the loop starts), return fast
    edgecase: when there's no head or head.next
"""
