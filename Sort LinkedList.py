# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or head.next is None:
            return head

        left = head
        right = self.midelement(head)
        temp = right.next
        right.next = None
        right = temp

        left = self.sortList(left)
        right = self.sortList(right)
        return self.merged(left, right)

    def midelement(self, head):
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def merged(self, left, right):
        T1 = Dummy = ListNode()
        while left and right:
            if left.val < right.val:
                T1.next = left
                T1 = left
                left = left.next
            else:
                T1.next = right
                T1 = right
                right = right.next

        if left:
            T1.next = left
        else:
            T1.next = right
        return Dummy.next















