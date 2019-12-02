#
# @lc app=leetcode id=94 lang=python3
#
# [94] Binary Tree Inorder Traversal
#
# https://leetcode.com/problems/binary-tree-inorder-traversal/description/
#
# algorithms
# Medium (58.91%)
# Likes:    2171
# Dislikes: 96
# Total Accepted:    574.8K
# Total Submissions: 964.3K
# Testcase Example:  '[1,null,2,3]'
#
# Given a binary tree, return the inorder traversal of its nodes' values.
# 
# Example:
# 
# 
# Input: [1,null,2,3]
# ⁠  1
# ⁠   \
# ⁠    2
# ⁠   /
# ⁠  3
# 
# Output: [1,3,2]
# 
# Follow up: Recursive solution is trivial, could you do it iteratively?
# 
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # morris method
    def third(self, root):
        result = []
        current = root

        while current:
            if not current.left:
                result.append(current.val)
                current = current.right
            else:
                right_most_node = current.left
                while right_most_node.right:
                    right_most_node = right_most_node.right
                current, right_most_node.right = current.left, current
                right_most_node.right.left = None

        return result

    # iterative
    def second(self, root):
        if not root:
            return []

        result = []
        candidates = [root]

        while candidates:
            candidate = candidates.pop()
            if candidate.right:
                candidates.append(candidate.right)
            if candidate.left:
                candidates.append(TreeNode(candidate.val))
                candidates.append(candidate.left)
            else:
                result.append(candidate.val)

        return result

    # recursive
    def first(self, root):
        if not root:
            return []
        return self.first(root.left) + [root.val] + self.first(root.right)

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        # return self.first(root)
        return self.second(root)
        # return self.third(root)
        
# @lc code=end

