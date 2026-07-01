class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]: 
        stored = {}
        for index, num in enumerate(nums):
            check = target - num
            if check in stored:
                return [stored[check], index]
            else:
                stored[num] = index