
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: [ListNode], val: int):
        fakenode = ListNode()
        first = fakenode
        temp = head
        fakenode.next = temp
        while temp:
            up_nxt = temp.next
            if temp.val == val:
                first.next = up_nxt
                # temp = up_nxt
            else:
                first = temp
                # temp = up_nxt
            temp = up_nxt

        return fakenode.next