from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.max_l = 0
        self.nl = []

    def maxDepth_v1(self, root: Optional[TreeNode]) -> int:
        print(f'{root=}')
        if root is None:
            return 0
        a = self.__print_tree(root, 0)
        print(f'{self.nl=}')
        return self.max_l

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        hl = self.maxDepth(root.left)
        hr = self.maxDepth(root.right)
        return max(hl, hr) + 1

    def __print_tree(self, tn: TreeNode, max_l):
        self.nl.append(tn.val)
        max_l = max_l + 1
        if tn.left is not None:
            self.__print_tree(tn.left, max_l)
        if tn.right is not None:
            self.__print_tree(tn.right, max_l)
        if tn.right is None and tn.left is None:
            print(f'{max_l=}')
            if self.max_l < max_l:
                self.max_l = max_l
            return