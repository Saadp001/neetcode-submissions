class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # convert to set for O(1) lookup
        numSet = set(nums)
        maxi = 0

        for num in numSet:
            # only start counting if num is a sequence start
            # i.e. no previous element exists
            if num - 1 not in numSet:
                length = 1

                # count forward, each check is O(1)
                while num + length in numSet:
                    length += 1

                # update answer
                maxi = max(maxi, length)

        return maxi