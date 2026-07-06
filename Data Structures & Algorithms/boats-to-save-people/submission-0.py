class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        n = len(people)
        h = n-1  #heaviest
        l = 0  # lightest
        cnt = 0
        while l<=h:
            if people[h] + people[l] <= limit:
                l +=1
                h-=1
                cnt+=1
            else:
                h-=1  
                cnt+=1  
        
        return cnt