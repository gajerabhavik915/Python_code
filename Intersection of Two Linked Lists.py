# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode):
        lenA = 0
        temp = headA
        while temp:
            lenA += 1
            temp = temp.next

        lenB = 0
        tempB = headB
        while tempB:
            lenB += 1
            tempB = tempB.next

        if lenB > lenA:
            skip = lenB - lenA
            startingB = headB
            while skip > 0:
                startingB = startingB.next
                skip -= 1

            startingA = headA
            while startingA != startingB:
                startingA = startingA.next
                startingB = startingB.next
            return startingA

        else:
            skip = lenA - lenB
            startingA = headA
            while skip > 0:
                startingA = startingA.next
                skip -= 1

            startingB = headB
            while startingB != startingA:
                startingA = startingA.next
                startingB = startingB.next
            return startingA
