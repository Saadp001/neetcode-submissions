class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest = min(strs, key=len)
        for char in range(len(shortest)):
            for s in strs:
                if s[char] != shortest[char]:
                    return shortest[:char]

        return shortest