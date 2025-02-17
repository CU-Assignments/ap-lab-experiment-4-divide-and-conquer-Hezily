class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            n = n & (n - 1)  # Remove the rightmost set bit
            count += 1
        return count

# Example usage:
solution = Solution()

# Test cases
print(solution.hammingWeight(11))  # Output: 3 (Binary: 1011)
print(solution.hammingWeight(128))  # Output: 1 (Binary: 10000000)
print(solution.hammingWeight(2147483645))  # Output: 30 (Binary: 111111111111111111111111111111)
