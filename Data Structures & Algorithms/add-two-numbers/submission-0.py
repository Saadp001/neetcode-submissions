class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy
        carry = 0

        while l1 or l2 or carry:
            # get values, 0 if list is exhausted
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            # add digits + carry
            total = v1 + v2 + carry
            carry = total // 10
            digit = total % 10

            # create new node with digit
            curr.next = ListNode(digit)
            curr = curr.next

            # advance pointers if not exhausted
            if l1: l1 = l1.next
            if l2: l2 = l2.next

        return dummy.next