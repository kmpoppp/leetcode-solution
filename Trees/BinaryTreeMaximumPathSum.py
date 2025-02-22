class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = -float('inf')

        def dfs(node):
            nonlocal ans
            if not node:
                return 0
            
            left_sum = dfs(node.left)
            right_sum = dfs(node.right)
            ans = max(ans, node.val + left_sum + right_sum)
            return max(0, max(left_sum, right_sum) + node.val)
        
        dfs(root)
        return ans
    
##Question Link : https://leetcode.com/problems/binary-tree-maximum-path-sum/
##Time Complexity : O(n)
##Space Complexity : O(h)