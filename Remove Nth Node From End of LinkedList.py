# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: [ListNode], n: int):
        len = 0
        temp = head
        while temp:
            len += 1
            temp = temp.next

        skip = len - n
        Dummy = ListNode()
        Dummy.next = head
        before = Dummy
        temp = head
        while temp:
            after = temp.next
            if skip == 0:
                before.next = after
                return Dummy.next
            else:
                before = temp
                temp = after
                skip -= 1

