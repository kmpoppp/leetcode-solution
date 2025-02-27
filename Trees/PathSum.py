class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        def dfs(head,Sum):
            if not head:
                return False
            Sum += head.val
            if not head.left and not head.right:
                return Sum == targetSum
            return dfs(head.left,Sum) or dfs(head.right,Sum)
        return dfs(root,0)
    
##Question Link : https://leetcode.com/problems/path-sum/
##Time Complexity : O(n)
##Space Complexity : O(h)