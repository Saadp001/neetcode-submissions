class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = head
        cnt = 0
        while temp:
            cnt+=1
            temp = temp.next

        if cnt ==1 and n ==1:
            return
            


        prev = None
        curr = head
        i = 0
        for i in range(cnt):
            if i == (cnt-n):            
                prev.next = curr.next
            else:
                prev = curr
                curr = curr.next    
               
        return head
          


                 
                

