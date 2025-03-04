class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        n = len(s1)
        l = 0
        c1 = [0]*26
        c2 = [0]*26
        for r in range(n):
            c1[ord(s1[r])-ord('a')] +=1
        for r in range(n):
            c2[ord(s2[r])-ord('a')] +=1
        if c1 == c2:
            return True
        for r in range(n,len(s2)):
            l+=1
            c2[ord(s2[l-1])-ord('a')] -=1
            c2[ord(s2[r])-ord('a')] +=1
            if c1 == c2:
                return True
        return False
    
##Question Link : https://leetcode.com/problems/permutation-in-string/
##Time Complexity : O(n+m)
##Space Complexity : O(1)