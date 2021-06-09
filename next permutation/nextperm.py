class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        nums_len = len(nums)
        for i in range(nums_len-1, 0, -1):
            if nums[i] > nums[i-1]:
                break
        else:
            i = 0
        l, r = i, nums_len-1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l+1, r-1
        if not i:
            return
        for j in range(i, nums_len):
            if nums[j] > nums[i-1]:
                break
        nums[i-1], nums[j] = nums[j], nums[i-1]
        return