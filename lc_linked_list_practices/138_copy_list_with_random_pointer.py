"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        curr = head
        dic = {}
        while curr:
            dic[curr] = Node(curr.val)
            curr = curr.next

        curr = head
        while curr:
            dic[curr].next = dic[curr.next] if curr.next else None
            # if curr.random:
            dic[curr].random = dic[curr.random] if curr.random else None
            curr = curr.next

        return dic[head]

    # def copyRandomList(self, head: 'Node') -> 'Node':
    #     if head is None: return None
    #     mapping = {}
    #     cur = head
    #     while cur:
    #         mapping[cur] = Node(cur.val,None,None)
    #         cur = cur.next
    #     cur = head
    #     while cur:
    #         if cur.next:
    #             mapping[cur].next = mapping[cur.next]
    #         if cur.random:
    #             mapping[cur].random = mapping[cur.random]
    #         cur = cur.next
    #     return mapping[head]
