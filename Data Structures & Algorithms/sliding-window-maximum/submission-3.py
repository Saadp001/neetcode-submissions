class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        i = 0
        
        ans = []
        # if len(nums) == 1:
        #     ans.append(nums[0])
        #     return ans
                
        # elif len(nums) == 2:
        #     ans.append(nums[i])
        #     ans.append(nums[i+1])
        #     return ans
            


        while i < (len(nums) - k) + 1:
            maxi = nums[i]

            maxi = max(nums[i:i+k])
            ans.append(maxi)
            i+=1
                 

        return ans   
        