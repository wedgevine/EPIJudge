#
# @lc app=leetcode id=145 lang=python3
#
# [145] Binary Tree Postorder Traversal
#
# https://leetcode.com/problems/binary-tree-postorder-traversal/description/
#
# algorithms
# Hard (50.62%)
# Likes:    1220
# Dislikes: 65
# Total Accepted:    308.5K
# Total Submissions: 601.9K
# Testcase Example:  '[1,null,2,3]'
#
# Given a binary tree, return the postorder traversal of its nodes' values.
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
# Output: [3,2,1]
# 
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

    # iterative
    def second(self, root):
        if not root:
            return []

        result = []
        candidates = [root]
        while candidates:
            candidate = candidates.pop()
            if not candidate.left and not candidate.right:
                result.append(candidate.val)
            else:
                candidates.append(TreeNode(candidate.val))
                if candidate.right:
                    candidates.append(candidate.right)
                if candidate.left:
                    candidates.append(candidate.left)
        
        return result

    # recursive
    def first(self, root):
        if not root:
            return []
        return self.first(root.left) + self.first(root.right) + [root.val]

    def postorderTraversal(self, root: TreeNode) -> List[int]:
        # return self.first(root)
        return self.second(root)

# @lc code=end

