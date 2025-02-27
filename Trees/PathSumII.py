class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = []
        def dfs(root,Sum,temp):
            nonlocal ans
            if not root:
                return
            Sum += root.val
            temp.append(root.val)
            if not root.left and not root.right:
                if Sum == targetSum:
                    ans.append(temp)
                return
            copyL,copyR = temp.copy(),temp.copy()
            dfs(root.left,Sum,copyL)
            dfs(root.right,Sum,copyR)
        dfs(root,0,[])
        return ans

##Question Link : https://leetcode.com/problems/path-sum-ii/
##Time Complexity : O(n)
##Space Complexity : 