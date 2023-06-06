# Definition for a binary tree node.
'''
try to solve through phase
Created temp list to add all element of that phase
once phase over, maxdepth(count) will be increased by one
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: [TreeNode]) -> int:
        queue = [root]

        maxdepth = 0
        while queue:
            len_queue = len(queue)
            temp = []
            for _ in range(len_queue):
                node = queue.pop(0)
                if node:
                    temp.append(node)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
            if temp:
                maxdepth += 1
        return maxdepth


