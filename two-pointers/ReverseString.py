class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i = 0 ##initial at left
        j = len(s)-1##initial at right
        while i<=j: ## squeeze
            s[i], s[j] = s[j] , s[i] ##swap left with right
            i+=1##move left
            j-=1##move right
            
##Question Link : https://leetcode.com/problems/reverse-string/description/
## Time Complexity : O(n)
## Space Complexity : O(1)