class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]: 
        stored = {}
        for i, num in enumerate(nums):
            check = target - num
            if check in stored:
                return [stored[check], i]
            stored[num] = i