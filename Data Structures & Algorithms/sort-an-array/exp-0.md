Intuition for selection sort: split the array into a "sorted" part (front) and "unsorted" part (rest). On each pass, find the **minimum of the unsorted part** and swap it into the front of that unsorted region. Repeat, shrinking the unsorted region each time.

So the core sub-problem you're stuck on — "find the min element in a range" — needs its own mini-loop: track an index `minIdx`, start it at the current position, then scan the rest comparing values and updating `minIdx` whenever you find something smaller.

```python
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n):
            minIdx = i
            for j in range(i+1, n):
                if nums[j] < nums[minIdx]:
                    minIdx = j
            nums[i], nums[minIdx] = nums[minIdx], nums[i]
        return nums
```

Walk through why: outer loop `i` is "which position am I filling next." Inner loop `j` scans everything after `i` to find the smallest value's **index** (not the value itself — you need the index so you can swap). `minIdx` starts as `i` (assume current position already holds the min), and updates only when something smaller is found. After the inner loop finishes, `minIdx` points to wherever the true minimum is in `nums[i:]`, and the swap puts it at position `i`.

**Trace** on `[5,3,1,4]`:
`i=0`: scan j=1..3, minIdx ends at 2 (value 1). Swap nums[0],nums[2] → `[1,3,5,4]`
`i=1`: scan j=2..3, minIdx ends at 1 itself (3 is smallest of 3,5,4)... 

Trace it yourself from here — what happens at `i=1`, `i=2`? That'll confirm you've got it.

**Complexity:** O(n²) time always (even if already sorted, you still scan everything), O(1) space — sorts in place.
