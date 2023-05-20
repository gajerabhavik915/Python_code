# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def zigzagLevelOrder(self, root: [TreeNode]) -> :
        result = []
        que = collections.deque()  # this is for creating queue
        que.append(root)
        count = 1
        while que:
            len_que = len(que)
            append_list = []
            for i in range(len_que):
                node = que.popleft()

                if node:
                    append_list.append(node.val)
                    que.append(node.left)
                    que.append(node.right)

            def reverse(list1):
                if len(list1) == 2:
                    list1[0], list1[1] = list1[1], list1[0]
                    return list1
                elif len(list1) > 2:
                    list1 = [i for i in list1[::-1]]
                    return list1
                else:
                    return list1

            if append_list and count % 2 != 0:
                result.append(append_list)
                count = count + 1
            elif append_list:
                # append_list =
                result.append(reverse(append_list))
                count = count + 1

        return result




