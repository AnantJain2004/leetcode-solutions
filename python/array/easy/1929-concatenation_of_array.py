from typing import List

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums + nums

if __name__ == "__main__":
    # Example test case
    nums = [1, 2, 1]
    
    solution = Solution()
    result = solution.getConcatenation(nums)
    
    print("Input:", nums)
    print("Output:", result)