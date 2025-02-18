class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        Hash = {}
        for i in range(len(nums)):
            if target-nums[i] in Hash:
                return [Hash[target-nums[i]],i]
            Hash[nums[i]] = i

## Question Link : https://leetcode.com/problems/two-sum/description/
## Time Complexity : O(n)
## Space Complexity : O(n)