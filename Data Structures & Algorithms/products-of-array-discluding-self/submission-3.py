class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        sum = 1
        ans = list()
        for i in range(len(nums)):
            sum = sum*nums[i]
        for j in range(len(nums)):
            ans.append(sum//nums[j])
        return ans  


# WHY IT'S FAILING

# 1. ZeroDivisionError (Logic Crash)The Problem: 
# You use sum // nums[j].Why it fails: If the input list contains a zero (e.g., [1, 2, 0, 4]), nums[j] will eventually be 0. 
# Dividing by zero causes the program to crash instantly.

# 2. Violation of Problem ConstraintsThe Problem: The standard LeetCode description for Product of Array Except Self explicitly states:
#  "You must write an algorithm that runs in O(n) time and without using the division operation." Your approach relies entirely on division.
                
        