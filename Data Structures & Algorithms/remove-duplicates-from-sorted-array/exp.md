Okay let's build it step by step.

**The array is sorted**, so duplicates are always next to each other:
```
[1, 1, 2, 3, 4]
      ^--- 1 appears twice, they're adjacent
```

So you only need to ask one question at each step: **"is this element different from the previous one?"** If yes → it's unique, keep it. If no → skip it.

**Where does `k` start?**
The first element is always unique (nothing before it to duplicate). So `k` starts at `1` — position 0 is already "kept".

**The loop:**
Start `i` at `1` (first element that could possibly be a duplicate), go till end:
```python
for i in range(1, n):
    if nums[i] != nums[i-1]:   # different from previous = unique
        nums[k] = nums[i]       # keep it
        k += 1
```

**Trace on** `[1,1,2,3,4]`, `k=1`:

`i=1`: `nums[1]=1 == nums[0]=1` → duplicate, skip
`i=2`: `nums[2]=2 != nums[1]=1` → unique, `nums[1]=2`, `k=2`
`i=3`: `nums[3]=3 != nums[2]=2` → unique, `nums[2]=3`, `k=3`
`i=4`: `nums[4]=4 != nums[3]=3` → unique, `nums[3]=4`, `k=4`


`k` is not storing anything — it's just a **position/index**. The unique elements are being written directly into `nums` itself.

Think of it like this — `nums` has two regions:

```
[1, 1, 2, 3, 4]
 ^              
 k=1 (everything before k is already "clean/unique")
```

As you find unique elements, you **overwrite** the front of `nums` with them:

```
Start:   [1, 1, 2, 3, 4]   k=1
                            (position 0 already kept, k points to next write spot)

i=1: 1==1, duplicate, skip
          [1, 1, 2, 3, 4]   k=1 (unchanged)

i=2: 2!=1, unique!
     write nums[k]=nums[i] → nums[1]=2
          [1, 2, 2, 3, 4]   k=2

i=3: 3!=2, unique!
     write nums[k]=nums[i] → nums[2]=3
          [1, 2, 3, 3, 4]   k=3

i=4: 4!=3, unique!
     write nums[k]=nums[i] → nums[3]=4
          [1, 2, 3, 4, 4]   k=4
```

See what happened? The **first k elements** `[1,2,3,4]` are all unique. The garbage `4` at the end doesn't matter — the problem only checks the first `k` positions.

`k` is simultaneously:
- the **write position** (where to put the next unique element)
- the **count** of unique elements found so far

That's why you return `k` at the end.

Return `k=4` ✓

Now write the full solution yourself — just add the `k=1` initialization and the `return` line.
