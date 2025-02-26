class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        maxP = [-float('inf'),1]
        q = deque()
        q.append(root)
        i = 1
        ans = 0
        while q:
            temp = 0
            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                temp+=node.val
            if temp>maxP[0]:
                maxP = [temp,i]
            i+=1
        return maxP[1]

##Question Link : https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/
##Time Complexity : O(n)
##Space Complexity : O(n)

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        maxP = [-float('inf'),1]
        q = deque()
        q.append(root)
        i = 1
        ans = 0
        while q:
            temp = sum(node.val for node in q)
            if temp>maxP[0]:
                maxP = [temp,i]
            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            i+=1
        return maxP[1]

##Question Link : https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/
##Time Complexity : O(n)
##Space Complexity : O(n)