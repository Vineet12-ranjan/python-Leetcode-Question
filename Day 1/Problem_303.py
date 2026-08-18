class NumArray:

    def __init__(self, nums):
        # Create prefix sum array
        self.prefix = [0]

        for num in nums:
            self.prefix.append(self.prefix[-1] + num)

    def sumRange(self, left, right):
        # Return sum from left to right
        return self.prefix[right + 1] - self.prefix[left]


# Example
nums = [-2, 0, 3, -5, 2, -1]

obj = NumArray(nums)

print(obj.sumRange(0, 2)) 
print(obj.sumRange(2, 5))  
print(obj.sumRange(0, 5)) 
