# Result: ACCEPTED
# Runtime: 6445ms

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        len_nums = len(nums)
        for int_one in xrange(0, len_nums):
            for int_two in xrange(int_one+1, len_nums):
                if nums[int_one] + nums[int_two] == target:
                    return [int_one, int_two]
                    