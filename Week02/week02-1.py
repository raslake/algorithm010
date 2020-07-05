##python 两数之和
class Solution(object):
    def twoSum(self, nums, target):
        lens = len(nums)
        for i  in range(1, lens):
            if (target - nums[i]) in nums and nums.index(target-nums[i]) == i:
                continue
            if (target - nums[i]) in nums and nums.index(target-nums[i]) != i:
		        j = nums.index(target-nums[i])
	                return (i,j)