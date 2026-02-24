[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# Sum Root To Leaf Binary Numbers - Python

This repository provides a clean, well-tested Python implementation for the LeetCode problem "Sum of Root to Leaf Binary Numbers". The solution uses a simple DFS to accumulate binary numbers along root-to-leaf paths and returns their sum.

## Problem link

https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/

## Quickstart

Prerequisites: Python 3.8+.

Install dependencies (pytest for running tests):

```
pip install -r requirements.txt
```

Run tests:

```
pytest
```

## Architecture

- sum_root_to_leaf.py: Core algorithm and TreeNode definition.
- tests/test_sum_root_to_leaf.py: Comprehensive test suite using pytest.
- requirements.txt: Project dependencies.

## Complexity

- Time complexity: O(N) where N is the number of nodes in the tree.
- Space complexity: O(H) due to recursion stack, where H is the tree height.

## Open Source & Contributions

This project is open source under the MIT license. Contributions are welcome.

## References

- LeetCode problem: https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/
