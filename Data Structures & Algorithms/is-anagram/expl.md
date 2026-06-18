**The dict mechanics first**, since that's the new part.

`check = {}` creates an empty dict — no keys yet. `check[key]` to assign always works whether the key exists or not: if it doesn't exist, it gets created; if it does, it gets overwritten. That's different from accessing `check[key]` to *read* a value — reading a key that doesn't exist throws `KeyError`.

`check.get(s[i], 0)` is a safe read: "give me `check[s[i]]` if it exists, otherwise give me `0` instead of crashing." That's exactly what you need here, because the first time you see a character you don't have an entry for it yet — `check.get('a', 0)` returns `0` instead of erroring, so `+1` on top of that gives `1`.

**Walking the code**

```python
check[s[i]] = check.get(s[i], 0) + 1
```
Read current count for this char from `s` (or 0 if unseen), add 1, store it back. This is incrementing a counter using a dict as your counter storage.

```python
check[t[i]] = check.get(t[i], 0) - 1
```
Same thing but subtracting, for the char from `t`.

Since both lines write into the *same* `check` dict, a character that shows up in both `s` and `t` gets `+1` then `-1` (or `-1` then `+1`) on the same key — they cancel out. A character that's overrepresented in one string ends up net positive or net negative.

**Trace**: `s="ab"`, `t="ba"`
`i=0`: `check['a'] = 0+1 = 1` (from s), `check['b'] = 0-1 = -1` (from t) → `check = {'a':1, 'b':-1}`
`i=1`: `check['b'] = -1+1 = 0` (from s), `check['a'] = 1-1 = 0` (from t) → `check = {'a':0, 'b':0}`

All zeros → `all(v==0 for v in check.values())` returns `True`.

If `t` had an extra `'c'` instead of matching `'a'`, that key would end at `-1`, not `0`, and `all(...)` would catch it and return `False`.

**Why this beats two separate counters**: same result as building `Counter(s)` and `Counter(t)` and comparing them, but you do it in one pass with one dict instead of two passes with two dicts — fewer objects, same correctness.

**Complexity**: O(n) time — one loop over the string length. O(k) space where k is the number of distinct characters across both strings (capped at 26 for lowercase letters, so technically O(1) if you know the alphabet is fixed, O(n) worst case in general).
