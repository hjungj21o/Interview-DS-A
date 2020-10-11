# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        prev, curr = dummy, head

        while curr:
            if curr.val == val:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next

        return dummy.next


"""
    Pseudocode:
        create a dummy node. link it to the input list
        create a prev and curr node, curr pointing to head and prev pointing to dummy
        create a loop to iterate through list
            if curr's val == input val, prev's next == prev.next.next
        return dummy.next
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        #edge case
        if not head:
            return None
        #create a dummy, link it to head
        dummy = ListNode(0)
        dummy.next = head

        #create a curr var
        curr = dummy

        #create a loop to iterate through input list
        while curr.next:
            #the if logic goes here
            if curr.next.val == val:
                curr.next = curr.next.next
            else:
                #move curr along the list
                curr = curr.next

        return dummy.next


"""
    we need to be looking one step ahead
    
    create a dummy, link it to head
    create a curr var, pointing to dummy
     
    create a loop to iterate through input node
        look one ahead, so if curr.next == val, then curr.next should == curr.next.next
        
    return dummy.next
    edge case: if there's no head
    time = O(n) b/c we're iterating through the list once
    space = O(1) b/c anything we create isn't affected by the input size
"""
