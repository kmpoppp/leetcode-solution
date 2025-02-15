class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        minP = float('inf')
        for i in range(len(nums)):
            if i>0 and nums[i] == nums[i-1]:
                continue
            l,r = i+1,len(nums)-1
            while l<r:
                sumP = nums[i]+nums[l]+nums[r]
                if sumP == target:
                    return sumP
                if sumP > target:
                    if abs(sumP-target) <= abs(minP-target):
                        minP = sumP
                    r-=1
                else:
                    if abs(sumP-target) <= abs(minP-target):
                        minP = sumP
                    l+=1
            
        return minP

## Question Link : https://leetcode.com/problems/3sum-closest/description/
## Time Complexity : O(n^2)
## Space Complexity : O(1)