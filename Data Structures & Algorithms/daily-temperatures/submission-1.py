class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0] * n
        stack = []  # stores indices

        for i in range(n):
            # pop all indices whose temperature is less than current
            while stack and temperatures[i] > temperatures[stack[-1]]:
                idx = stack.pop()
                ans[idx] = i - idx  # days to wait = current index - popped index
            stack.append(i)

        return ans