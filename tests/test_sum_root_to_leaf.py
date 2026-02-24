import pytest
from sum_root_to_leaf import TreeNode, sum_root_to_leaf


def test_empty_tree():
    assert sum_root_to_leaf(None) == 0


def test_single_node_tree():
    root = TreeNode(1)
    assert sum_root_to_leaf(root) == 1


def test_example_1():
    # Tree: [1,0,1,0,1,0,1]
    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(1)
    root.left.left = TreeNode(0)
    root.left.right = TreeNode(1)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(1)
    assert sum_root_to_leaf(root) == 22


def test_example_2_single_zero():
    root = TreeNode(0)
    assert sum_root_to_leaf(root) == 0


def test_skewed_left():
    # 1 -> 0 -> 0 (path: 100 -> 4)
    root = TreeNode(1, TreeNode(0, TreeNode(0)))
    assert sum_root_to_leaf(root) == 4


def test_skewed_right_short():
    # 1 -> right -> 1 (path: 11 -> 3)
    root = TreeNode(1, None, TreeNode(1))
    assert sum_root_to_leaf(root) == 3


def test_invalid_value_raises():
    root = TreeNode(2)
    with pytest.raises(ValueError):
        sum_root_to_leaf(root)
