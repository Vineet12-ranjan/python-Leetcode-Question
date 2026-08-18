class Solution:
    def findMaxAverage(self, nums, k):
        # Sum of first k elements
        window_sum = sum(nums[:k])

        # Maximum sum found so far
        max_sum = window_sum

        # Slide the window
        for i in range(k, len(nums)):
            window_sum += nums[i]
            window_sum -= nums[i - k]

            max_sum = max(max_sum, window_sum)

        # Return maximum average
        return max_sum / k


# Example
nums = [1, 12, -5, -6, 50, 3]
k = 4

obj = Solution()

print(obj.findMaxAverage(nums, k))