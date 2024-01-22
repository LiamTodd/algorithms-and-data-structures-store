from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getLeafSeq(self, node, seq):
        # DFS, tracking the leafs

        # Base case: node is a leaf
        if not (node.left or node.right):
            seq.append(node.val)

        # Recursive cases: left first
        if node.left:
            self.getLeafSeq(node.left, seq)
        if node.right:
            self.getLeafSeq(node.right, seq)

    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        seq_1 = []
        seq_2 = []
        self.getLeafSeq(root1, seq_1)
        self.getLeafSeq(root2, seq_2)

        return seq_1 == seq_2
