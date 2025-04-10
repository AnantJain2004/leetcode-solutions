from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        left, right = 0, len(s)-1
        while left < right :
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

# Test Cases
def test_reverse_string():
    sol = Solution()

    s1 = ["h", "e", "l", "l", "o"]
    sol.reverseString(s1)
    print("Test 1:", s1) # Expected: ['o', 'l', 'l', 'e', 'h']

    s2 = ["H", "a", "n", "n", "a", "h"]
    sol.reverseString(s2)
    print("Test 2:", s2)  # Expected: ['h', 'a', 'n', 'n', 'a', 'H']

    s3 = ["A"]
    sol.reverseString(s3)
    print("Test 3:", s3)  # Expected: ['A']

    s4 = []
    sol.reverseString(s4)
    print("Test 4:", s4)  # Expected: []

test_reverse_string()