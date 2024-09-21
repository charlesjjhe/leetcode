from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        pl = []
        ql = []
        self.get_flat(p, pl)
        self.get_flat(q, ql)
        return pl == ql

    def get_flat(self, r: Optional[TreeNode], fl: List):
        if r is None:
            return
        fl.append(r.val)
        if r.left is not None:
            self.get_flat(r.left, fl)
        else:
            fl.append(None)
        if r.right is not None:
            self.get_flat(r.right, fl)
        else:
            fl.append(None)
