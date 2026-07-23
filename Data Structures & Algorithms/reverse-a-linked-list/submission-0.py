# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        i = head
        while i:
            arr.append(i.val)
            i = i.next
        
        rev = arr[::-1]

        dummy = ListNode(0)
        curr = dummy
        
        for val in rev:
            curr.next = ListNode(val)
            curr = curr.next

        return dummy.next    


      
        