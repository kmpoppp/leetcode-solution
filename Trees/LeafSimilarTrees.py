class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        ans = [[],[]]
        def dfs(root,n):
            nonlocal ans
            if not root:
                return
            if not root.left and not root.right:
                ans[n].append(root.val)
            dfs(root.left,n)
            dfs(root.right,n)
        dfs(root1,0)
        dfs(root2,1)
        if ans[0] == ans[1]:
            return True
        return False
    
##Question Link : https://leetcode.com/problems/leaf-similar-trees/description/
##Time Complexity : O(n)
##Space Complexity : O(n)