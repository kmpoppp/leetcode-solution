class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) <3:
            return []
        if len(nums) ==3:
            if sum(nums)==0:
                return [nums]
        nums.sort()
        ans = []
        for i,n in enumerate(nums):
            if nums[i] == nums[i-1] and i>0:
                continue
            l,r = i+1,len(nums)-1
            while l <r :
                tsum = nums[l]+nums[r]+n
                if tsum > 0:
                    r-=1
                elif tsum < 0:
                    l+=1
                else:
                    ans.append([n,nums[l],nums[r]])
                    l+=1
                    while nums[l] == nums[l-1] and l<r :
                        l+=1
        return ans
    
## Question Link : https://leetcode.com/problems/3sum/description/
## Time Complextiy : O(n^2)
## Space Complexity : O(n)