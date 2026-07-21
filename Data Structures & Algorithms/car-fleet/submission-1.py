class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
            mp = {}
            
            for i in range(len(position)):
                mp[position[i]] = speed[i]

            sorted_mp = dict(sorted(mp.items()))    

            stack = []
            time = []
          
            for key, value in sorted_mp.items():
                t = (target - key)/value
                time.append(t)

            for t in time:
                if not stack or t < stack[-1]:
                    stack.append(t)

            return len(stack)        

                  


              

            


