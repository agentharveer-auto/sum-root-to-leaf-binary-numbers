"""
Tree and function for Sum of Root to Leaf Binary Numbers.
"""

from __future__ import annotations

from typing import Optional

class TreeNode:
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None) -> None:
        self.val = val
        self.left = left
        self.right = right


def sum_root_to_leaf(root: Optional[TreeNode]) -> int:
    """
    Calculate the sum of numbers represented by root-to-leaf paths where each node contains 0/1.
    Each path yields a binary number with the root as the most significant bit.
    """
    total = 0

    def dfs(node: Optional[TreeNode], current: int) -> None:
        nonlocal total
        if node is None:
            return
        if node.val not in (0, 1):
            raise ValueError("Node value must be 0 or 1")
        current = (current << 1) | node.val
        if node.left is None and node.right is None:
            total += current
        else:
            dfs(node.left, current)
            dfs(node.right, current)

    dfs(root, 0)
    return total

__all__ = ["TreeNode", "sum_root_to_leaf"]
