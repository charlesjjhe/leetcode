from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        id_set = set()
        while head:
            if head in id_set:
                return True
            else:
                id_set.add(head)
                head = head.next
        return False


