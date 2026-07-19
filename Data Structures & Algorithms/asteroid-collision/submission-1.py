class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for a in asteroids:
            # keep colliding while:
            # current asteroid is negative AND top of stack is positive
            while stack and a < 0 and stack[-1] > 0:
                if stack[-1] < abs(a):
                    stack.pop()      # top destroyed, current survives, keep colliding
                elif stack[-1] == abs(a):
                    stack.pop()      # both destroyed
                    a = 0            # mark current as destroyed
                    break
                else:
                    a = 0            # current destroyed, top survives
                    break

            if a != 0:
                stack.append(a)     # current survived, push it

        return stack