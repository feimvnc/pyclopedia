""" 
Implement a linked list using insertion sort method.
"""


from hashlib import new
from operator import ne


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return str(self.val)


class Solution(object):
    def insertionSortList(self, head: ListNode) -> ListNode:
        dummy = ListNode(-1)
        cur = dummy
        while head:
            if cur and cur.val > head.val:
                cur = dummy
                print(cur.val)
            while cur.next and cur.next.val < head.val:
                cur = cur.next
                print(cur.val)
            cur.next, cur.next.next, head = head, cur.next, head.next
        return dummy.next


node = ListNode(0)
node.next = ListNode(2)
node.next.next = ListNode(5)
node.next.next.next = ListNode(6)
node.next.next.next.next = ListNode(3)

new_node = ListNode(8)
print(Solution().insertionSortList(node))
# print(Solution().insertionSortList(node.next.next))
