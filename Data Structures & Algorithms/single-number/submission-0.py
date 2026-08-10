class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a  = set(nums)
        for i in a:
            x = nums.pop()
            if x in nums:
                nums.remove(x)
            else: return x
        