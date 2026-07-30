# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # Phase 1: Set up dummy node to handle edge case where left = 1
        dummy = ListNode(0, head)
        leftprev = dummy
        curr = head
        
        # Move pointers to the starting reversal position
        for _ in range(left - 1):
            leftprev = curr
            curr = curr.next
            
        # Phase 2: Standard in-place reversal loop
        prev = None
        for _ in range(right - left + 1):
            temp = curr.next     # 1. Save next node
            curr.next = prev     # 2. Reverse link
            prev = curr          # 3. Shift prev forward
            curr = temp          # 4. Shift curr forward using the saved temp
            
        # Phase 3: Reconnect the sublist back into the main list
        # leftprev.next currently points to the old start of sublist (which is now the tail)
        leftprev.next.next = curr  # Connect tail of reversed section to the remaining list
        leftprev.next = prev       # Connect node before sublist to the new head of reversed section
        
        return dummy.next
