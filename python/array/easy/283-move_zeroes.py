from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        insert_pos = 0

        # Move all non-zero elements to the front
        for num in nums:
            if num != 0:
                nums[insert_pos] = num
                insert_pos += 1

        # Fill remaining positions with zeroes
        while insert_pos < len(nums):
            nums[insert_pos] = 0
            insert_pos += 1

# Test cases
def test():
    sol = Solution()

    nums1 = [0, 1, 0, 3, 12]
    sol.moveZeroes(nums1)
    print(nums1)  # Output: [1, 3, 12, 0, 0]

    nums2 = [0]
    sol.moveZeroes(nums2)
    print(nums2)  # Output: [0]

    nums3 = [1, 2, 3]
    sol.moveZeroes(nums3)
    print(nums3)  # Output: [1, 2, 3]

    nums4 = [0, 0, 1]
    sol.moveZeroes(nums4)
    print(nums4)  # Output: [1, 0, 0]

    nums5 = [0, 0, 0]
    sol.moveZeroes(nums5)
    print(nums5)  # Output: [0, 0, 0]

test()