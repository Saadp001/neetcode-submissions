Let's back up to intuition before fixing this specific line, because the approach itself has a deeper problem beyond this one bug.

**What are you trying to do?** Remove all instances of `val` from `nums`, in-place, and return the new length. The classic approach is two-pointer: one pointer (`k`) tracks where the next "keep" element should go, another pointer (`i`) scans through the array. When `nums[i] != val`, you copy it to `nums[k]` and advance `k`.

**Why your current approach breaks:** you're trying to mutate the list (`pop`) while also iterating over it with `range(n)`, where `n` was computed *before* the loop started. Once you `pop(i)`, the list is now shorter than `n`, but your loop still thinks there are `n` elements — `range(n)` doesn't know the list shrank. So `i+1` can point past the new, shorter list. That's the `IndexError`.

This is a general trap: **never delete from a list while iterating forward over indices computed from the original length.** Popping shifts every element after `i` left by one, which also messes with which elements you've already checked.

---

Try the two-pointer approach instead — no popping at all, just overwriting:

```python
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k
```

Trace it yourself on `nums = [3,2,2,3], val = 3` before running it — walk through what `k` and `nums` look like at each step. Want to try that, or do you want me to walk through it first?

`k` is not an array — it's just an integer, a pointer/index into `nums` itself. There's no second array being created. `nums` is being overwritten **in place**.

Trace on `nums = [3,2,2,3], val = 3`:

Start: `k = 0`, `nums = [3,2,2,3]`

`i=0`: `nums[0]=3`, equals val → skip, `k` stays 0
`i=1`: `nums[1]=2`, not val → `nums[0] = nums[1]` → `nums` becomes `[2,2,2,3]`. `k` becomes 1
`i=2`: `nums[2]=2`, not val → `nums[1] = nums[2]` → `nums` becomes `[2,2,2,3]` (no visible change since both were 2). `k` becomes 2
`i=3`: `nums[3]=3`, equals val → skip, `k` stays 2

Loop ends. `nums = [2,2,2,3]`, return `k = 2`.

The first `k` elements of `nums` (`nums[0]` and `nums[1]`, i.e. `[2,2]`) are the "kept" elements — exactly what the problem wants. Whatever's sitting in `nums[2:]` afterward is leftover garbage; the problem doesn't care what's there, it only checks the first `k` elements.

So `k` is doing two jobs: it's the **write position** (where the next valid element should go) and, once the loop ends, it doubles as the **count** of valid elements — which is exactly what the function needs to return.
