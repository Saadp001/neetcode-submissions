class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        res = max(weights)
        while True:
            ships = 1
            cap = res
            for w in weights:
                if cap - w < 0:
                    ships += 1
                    cap = res
                cap -= w

            if ships <= days:
                return res

            res += 1