class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        # The first element is already unique.
        # k points to the next position for a unique element.
        k = 1

        for i in range(1, len(nums)):
            # Compare the current element with
            # the last unique element.
            if nums[i] != nums[k - 1]:
                nums[k] = nums[i]
                k += 1

        return k
