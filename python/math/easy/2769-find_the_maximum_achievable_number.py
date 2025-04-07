class Solution:
    def theMaxAchievableNumberX(self, num: int, t: int) -> int:
        return num + 2 * t
    
# Example Usage
if __name__ == "__main__":
    solution = Solution()

    # Test Case 1
    num = 4
    t = 1
    result = solution.theMaxAchievableNumberX(num, t)
    print(f"Input: num = {num}, t = {t}")
    print(f"Output: {result}") # Expected: 6

    # Test Case 2
    num = 3
    t = 2
    result = solution.theMaxAchievableNumberX(num, t)
    print(f"Input: num = {num}, t = {t}")
    print(f"Output: {result}") # Expected: 7