# Definition for a binary tree node.

'''
Hint - Using recursion, first we will go to the bottom node
     - Check their balance on both side if it is balanced then go to above element.
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def helper(r):
    if r is None:
        return 0, True  # depth, is_balanced
    print(r.val, 'start')
    l, is_balanced_left = helper(r.left)  # 1, True
    print(r.val, 'left finished', l, is_balanced_left)
    ri, is_balanced_right = helper(r.right)  # 2, True
    print(r.val, 'right finished', ri, is_balanced_right)
    return 1 + max(l, ri), abs(l - ri) <= 1 and is_balanced_left and is_balanced_right


class Solution:
    def isBalanced(self, root: [TreeNode]) -> bool:
        _, is_balanced = helper(root)
        return is_balanced