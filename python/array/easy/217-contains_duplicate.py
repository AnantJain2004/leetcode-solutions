from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Returns True if any value appears at least twice
        # Returns False if every element is distinct
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
    
# Test Cases
def test():
    sol = Solution()

    nums1 = [1, 2, 3, 1]
    print(sol.containsDuplicate(nums1))  # Output: True

    nums2 = [1, 2, 3, 4]
    print(sol.containsDuplicate(nums2))  # Output: False

    nums3 = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    print(sol.containsDuplicate(nums3))  # Output: True

    nums4 = []
    print(sol.containsDuplicate(nums4))  # Output: False

    nums5 = [99]
    print(sol.containsDuplicate(nums5))  # Output: False

test()