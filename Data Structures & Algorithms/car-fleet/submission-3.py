class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = sorted(zip(position, speed), reverse= True)
        stack = []

        for po , sp in pairs:
            t = (target-po)/sp

            if not stack or stack[-1] < t:
                stack.append(t)
        return len(stack)        