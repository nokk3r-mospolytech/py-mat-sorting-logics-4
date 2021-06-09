class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        output = []
        nth_bit = 1 << n

        for i in range(2 ** n):
            bitmask = bin(i | nth_bit)[3:]
            output.append([nums[j] for j in range(n) if bitmask[j] == '1'])

        return output