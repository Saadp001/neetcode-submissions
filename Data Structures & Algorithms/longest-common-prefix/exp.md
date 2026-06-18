Idea first, since that's probably where you're stuck conceptually too: the common prefix can never be longer than the shortest string in the list. So pick the shortest string as your candidate, then check character by character whether every other string agrees with it at that position. The moment one disagrees, you cut the prefix there.

**Python syntax pieces you need:**

`min(strs, key=len)` — finds the shortest string in a list without writing a manual loop. `key=len` tells `min` to compare strings by their length instead of alphabetically.

Strings index just like lists: `s[i]` gets the character at position `i`.

`s[:i]` slices from the start up to (not including) index `i` — that's how you cut the prefix when a mismatch is found.

**Code:**
```python
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest = min(strs, key=len)
        for i in range(len(shortest)):
            for s in strs:
                if s[i] != shortest[i]:
                    return shortest[:i]
        return shortest
```

**Trace** on `["flower", "flow", "flight"]`:
`shortest = "flow"` (length 4, shortest of the three)
`i=0`: char `'f'`. All three strings have `'f'` at index 0. Continue.
`i=1`: char `'l'`. All three have `'l'` at index 1. Continue.
`i=2`: char `'o'`. `"flight"[2]` is `'i'`, not `'o'` → mismatch → return `shortest[:2]` = `"fl"`.

If the loop finishes without ever returning (every string agrees through the whole length of `shortest`), then `shortest` itself is the answer — that's the `return shortest` at the end.

**Complexity:** O(n·m) time where n is the number of strings and m is the length of the shortest one — worst case you check every character of every string once. O(1) extra space (ignoring the output string itself).

