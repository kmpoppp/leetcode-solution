class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        ans = []
        q = deque([root])
        while q:
            ans.append(sum(node.val for node in q))
            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        ans.sort(reverse=True)
        return ans[k-1] if k <= len(ans) else -1
    
##Question Link : https://leetcode.com/problems/kth-largest-sum-in-a-binary-tree/description/
##Time Complexity : O(nlogn)
##Space Complexity : O(h)