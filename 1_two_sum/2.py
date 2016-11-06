# Result: ACCEPTED
# Runtime: 49ms

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        processed = {nums[0]:0}
        for curr in xrange(1, len(nums)):
            if target - nums[curr] in processed:
                return [processed[target - nums[curr]], curr]
            processed[nums[curr]] = curr