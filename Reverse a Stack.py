
# User function Template for python3

from typing import List


class Solution:
    # method 1
    def reverse(self,st):
        if len(st) == 1:
            return st
        len1 = len(st)
        len2 = len(st)//2

        def recursion(st, len1, len2, index):
            if len1 == len2:
                return st
            st[len1-1], st[index] = st[index], st[len1-1]
            st = recursion(st, len1-1, len2, index+1)
            return st

        s = recursion(st, len1, len2, 0)
        return s

    # method 2
    def reverse(self, st):
        if len(st) == 1:
            return st
        len1 = len(st)
        len2 = len(st) // 2

        def recursion(st, len1, index):
            if index > len1:
                return st
            st[len1 - 1], st[index - 1] = st[index - 1], st[len1 - 1]
            st = recursion(st, len1 - 1, index + 1)
            return st

        s = recursion(st, len1, 1)
        return s
