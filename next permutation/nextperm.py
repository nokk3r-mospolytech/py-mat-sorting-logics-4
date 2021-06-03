class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        index = len(nums) - 2
        while index >= 0:
            if nums[index] < nums[index + 1]:
                break
            index -= 1
        if index < 0:
            nums.sort()
            return

        nextIndex = index + 1
        while nextIndex < len(nums) and nums[nextIndex] > nums[index]:
            nextIndex += 1

        nums[index], nums[nextIndex - 1] = nums[nextIndex - 1], nums[index]
        nums[index + 1:] = nums[index + 1:][::-1]
