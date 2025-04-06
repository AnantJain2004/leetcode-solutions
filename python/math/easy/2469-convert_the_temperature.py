from typing import List

class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        kelvin = celsius + 273.15
        fahrenheit = celsius * 1.80 + 32.00
        return [kelvin, fahrenheit]

# Example usage
if __name__ == "__main__":
    solution = Solution()

    # Test Case 1
    celsius = 36.50
    result = solution.convertTemperature(celsius)
    print(f"Input: {celsius}")
    print(f"Output: {result}")  # Expected: [309.65, 97.7]

    # Test Case 2
    celsius = 122.11
    result = solution.convertTemperature(celsius)
    print(f"\nInput: {celsius}")
    print(f"Output: {result}")  # Expected: [395.26, 251.798]