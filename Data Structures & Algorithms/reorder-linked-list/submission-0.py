class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # step 1 - collect all values
        arr = []
        curr = head
        while curr:
            arr.append(curr.val)
            curr = curr.next

        # step 2 - reorder values
        # 0,1,2,3,4 → 0,4,1,3,2
        result = []
        l, r = 0, len(arr) - 1
        while l <= r:
            if l == r:
                result.append(arr[l])
            else:
                result.append(arr[l])
                result.append(arr[r])
            l += 1
            r -= 1

        # step 3 - rebuild linked list
        curr = head
        for val in result:
            curr.val = val
            curr = curr.next