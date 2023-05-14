# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: [ListNode], left: int, right: int):
        # method 1
        dummy = ListNode()
        dummy.next = head
        pre = dummy
        temp = head
        len = right - left + 1
        if len == 1:
            return head

        while temp:
            if temp.val != left:
                pre = temp
                # print(temp.val)
                temp = temp.next

            else:
                left1 = temp
                print(left1.val)
                pre1 = None
                while len:
                    nxt = temp.next
                    temp.next = pre1
                    pre1 = temp
                    temp = nxt
                    len -= 1
                pre.next = pre1
                left1.next = temp
                return dummy.next

        # method 2

        # dummy = ListNode(0)
        # dummy.next = head
        # head1 = dummy
        # r = right-left+1
        # count_l = 1
        # left1 = head
        # while left1 and count_l < left:
        #     count_l = count_l + 1
        #     left1 = left1.next
        #     head1 = head1.next
        # left2 = left1
        # pre = None
        # for i in range(r):
        #     temp = left1.next
        #     left1.next = pre
        #     pre = left1
        #     left1 = temp

        # head1.next = pre
        # left2.next = left1

        # return dummy.next

