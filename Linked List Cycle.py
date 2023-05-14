# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: [ListNode]) -> bool:


        slow = fast = head
        if head is None:
            return False
        if head.next is None:
            return False

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False


        # behind = ahead = head
        # while behind and ahead and ahead.next:
        #     behind = behind.next
        #     ahead = ahead.next.next
        #     if behind == ahead:
        #         return True
        # else:
        #     return False
