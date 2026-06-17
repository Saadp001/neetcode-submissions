class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        check = {}
        for char in s:
            check[char] = check.get(char, 0) + 1

        for char in t:
            check[char] = check.get(char, 0) - 1

        return all(v == 0 for v in check.values())    