class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)


# Test Cases
if __name__ == "__main__":
    sol = Solution()

    # Test Case 1
    haystack = "sadbutsad"
    needle = "sad"
    print("Output:", sol.strStr(haystack, needle))  # Expected: 0

    # Test Case 2
    haystack = "leetcode"
    needle = "leeto"
    print("Output:", sol.strStr(haystack, needle))  # Expected: -1

    # Test Case 3
    haystack = "hello"
    needle = "ll"
    print("Output:", sol.strStr(haystack, needle))  # Expected: 2

    # Edge Case
    haystack = "a"
    needle = "a"
    print("Output:", sol.strStr(haystack, needle))  # Expected: 0
