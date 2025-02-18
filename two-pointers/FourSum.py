class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans = []
        n = len(nums)
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1,n):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                l,r = j+1,n-1
                while l < r:
                    fsum = nums[i]+nums[j]+nums[l]+nums[r]
                    if fsum > target:
                        r-=1
                    elif fsum < target:
                        l+=1
                    else:
                        ans.append([nums[i],nums[j],nums[l],nums[r]])
                        l+=1
                        r-=1
                        while l<r and nums[l] == nums[l-1] :
                            l+=1
        return ans
    
## Question Link : https://leetcode.com/problems/4sum/description/
## Time Complexity : O(n^3)
## Space Complexity : O(n)