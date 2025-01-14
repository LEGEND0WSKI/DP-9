# // Time Complexity :O(n^2)
# // Space Complexity :O(n^2) momomap
# // Did this code successfully run on Leetcode : Yes
# // Any problem you faced while coding this :No


# // Your code here along with comments explaining your approach


# dfs with memoisation 9908 ms
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        self.memo= [[-99999]*n for _ in range(n)]           
        return self.helper(nums, 0, -1)

    def helper(self, nums, idx, prevIdx):
        
        #basecase
        if idx == len(nums):
            return 0
        if self.memo[idx][prevIdx] != -99999:
            return self.memo[idx][prevIdx]

        #logic
        # choose
        case0 = self.helper(nums,idx +1, prevIdx)
        # dont choose
        case1 = 0
        if prevIdx == -1 or nums[idx] > nums[prevIdx]:
            case1 = 1 + self.helper(nums,idx+1,idx)

        self.memo[idx][prevIdx] = max(case0,case1)
        return self.memo[idx][prevIdx]
        