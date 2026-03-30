class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i, j in enumerate(nums):
            if j in map:
                return [map[j], i]
            else:
                map[target - j] = i