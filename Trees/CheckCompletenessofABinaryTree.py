## My 1st Approach (Kinda Brute Force)

class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        if not root.left and not root.right:
            return True
        def dfs(root):
            if not root:
                return 0
            return max(dfs(root.left),dfs(root.right))+1
        level = dfs(root)
        ans = []
        q = deque()
        q.append(root)
        i = 0
        b4last = []
        lengthlast = 0
        while q:
            ans.append([])
            for _ in range(len(q)):
                node = q.popleft()
                ans[-1].append(node.val)
                if i==level-2:
                    b4last.append(node)
                if i == level-1:
                    lengthlast +=1
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            i+=1
        for i in range(len(ans)-1):
            if len(ans[i]) != 2**i:
                return False
        count = lengthlast//2
        for i in range(len(b4last)):
            if count ==0 and lengthlast ==0:
                continue
            if count != 0 and not (b4last[i].left and b4last[i].right):
                return False
            if count == 0 and lengthlast == 1:
                if b4last[i].left:
                    return True
                if not b4last[i].left:
                    return False
            count -= 1
            lengthlast -= 2
        return True
    
##Question Link : https://leetcode.com/problems/kth-largest-sum-in-a-binary-tree/description/
##Time Complexity : O(n)
##Space Complexity : O(n)

## Optimized Approach

class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        q = deque([root])
        nullSeen = False
        while q:
            node = q.popleft()
            if node:
                if nullSeen:
                    return False
                q.append(node.left)
                q.append(node.right)
            else:
                nullSeen = True
        return True
    
##Question Link : https://leetcode.com/problems/kth-largest-sum-in-a-binary-tree/description/
##Time Complexity : O(n)
##Space Complexity : O(n)

