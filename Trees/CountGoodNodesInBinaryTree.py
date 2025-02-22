class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        def dfs(root,limit):
            nonlocal count
            if not root:
                return
            if root.val>=limit:
                count+=1
            l = max(limit,root.val)
            dfs(root.left,l)
            dfs(root.right,l)
        dfs(root,root.val)
        return count
    
##Question Link : https://leetcode.com/problems/count-good-nodes-in-binary-tree/description/
##Time Complexity : O(n)
##Space Complexity : O(h)