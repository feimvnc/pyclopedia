""" 
Reorder linked list like the following pattern,
pick one from head, pick one from tail, 
till all nodes are used.

Input:
L0→L1→...→Ln-1→Ln
Output: 
L0→Ln→L1→Ln-1→L2→Ln-2→...

Example:
{1,2,3,4}
{1,4,2,3}
"""


class Solution:
    def reorderList(self, head):
        if not head:
            return
        # split list, then reverse, the combine
        fast = slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        head1, head2 = head, slow.next
        slow.next = None
        # reverse
        cur, pre = head2, None
        while cur:
            nex = cur.next
            cur.next = pre
            pre = cur
            cur = nex
        # merge
        cur1, cur2 = head1, pre
        while cur2:
            nex1, nex2 = cur1.next, cur2.next
            cur1.next = cur2
            cur2.next = nex1
            cur1, cur2 = nex1, nex2
