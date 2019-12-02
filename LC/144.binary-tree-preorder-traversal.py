#
# @lc app=leetcode id=144 lang=python3
#
# [144] Binary Tree Preorder Traversal
#
# https://leetcode.com/problems/binary-tree-preorder-traversal/description/
#
# algorithms
# Medium (52.86%)
# Likes:    1039
# Dislikes: 46
# Total Accepted:    402.3K
# Total Submissions: 755.4K
# Testcase Example:  '[1,null,2,3]'
#
# Given a binary tree, return the preorder traversal of its nodes' values.
# 
# Example:
# 
# 
# Input: [1,null,2,3]
# ⁠  1
# ⁠   \
# ⁠    2
# ⁠   /
# ⁠  3
# 
# Output: [1,2,3]
# 
# 
# Follow up: Recursive solution is trivial, could you do it iteratively?
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    # morris?
    def third(self, root):
        result = []
        current = root

        while current:
            result.append(current.val)
            if not current.left:
                current = current.right
            else:
                right_most_node = current.left
                while right_most_node.right:
                    right_most_node = right_most_node.right
                current, right_most_node.right = current.left, current.right

        return result

    # iterative
    def second(self, root):
        if not root:
            return []

        result = []
        candidates = [root]

        while candidates:
            candidate = candidates.pop()
            result.append(candidate.val)
            if candidate.right:
                candidates.append(candidate.right)
            if candidate.left:
                candidates.append(candidate.left)

        return result

    # recursive
    def first(self, root):
        result = []

        if root:
            result = [root.val] + self.first(root.left) + self.first(root.right)
        
        return result

    def preorderTraversal(self, root: TreeNode) -> List[int]:
        # return self.first(root)
        # return self.second(root)
        return self.third(root)
        
# @lc code=end

