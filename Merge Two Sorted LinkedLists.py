# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: [ListNode], list2: [ListNode]):
        Dummy = ListNode()
        pre = Dummy

        while list1 and list2:
            if list1.val < list2.val:
                pre.next = list1
                pre = list1
                list1 = list1.next
            elif list1 == list2:
                pre.next = list2
                pre = list2
                list2 = list2.next
                pre.next = list1
                pre = list1
                list1 = list1.next
            else:
                pre.next = list2
                pre = list2
                list2 = list2.next

        if list1 is None:
            pre.next = list2
        else:
            pre.next = list1

        return Dummy.next