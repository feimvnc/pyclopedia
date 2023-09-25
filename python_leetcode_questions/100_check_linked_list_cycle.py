""" 
Check if a linked list has cycle.
When a null or None node is found, there is no cycle.
When there is a cycle, checking will go into infinite cycle.
Use two pointers, fast and slow, when fast catches slow, exit.
"""

from re import L


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def hasCycle(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next  # slow ptr
            fast = fast.next.next  # fast ptr
            if slow == fast:  # exit condition
                return True
        return False


node1 = ListNode(1)
node1.next = ListNode(2)
node1.next.next = ListNode(3)
node1.next.next.next = ListNode(4)
node1.next.next.next.next = ListNode(5)
node1.next.next.next.next.next = (
    node1.next
)  # cycle node, comment this line, non cycle list
print(Solution().hasCycle(node1))
