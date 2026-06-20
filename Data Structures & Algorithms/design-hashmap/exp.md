**Intuition:** A real hashmap normally needs collision handling (multiple keys hashing to the same bucket), which is where linked lists usually come in. But look at the constraints for this problem — keys are bounded, typically `0 <= key <= 10^6`. That means you don't need to *hash* anything at all. You can just use the key directly as an index into a big array.

**Brute force = direct indexing:**
- `put(key, value)`: store `value` at `array[key]`
- `get(key)`: read `array[key]`
- `remove(key)`: reset `array[key]` to some "empty" marker

The only design question: what do you put in the array initially, and what marker means "this key doesn't exist"? Since `value` itself can be any int including 0, you can't use 0 as the "empty" marker — you need something value can never be, like `-1` (if values are guaranteed non-negative) or a special sentinel.

**Syntax pieces you'll need:**
- `self.data = [-1] * (10**6 + 1)` — creates an array of a million+1 slots, all initialized to -1
- This goes in `__init__`, which is the constructor — runs once when `MyHashMap()` is created. Always takes `self` as first param.

---

Try writing it yourself: `__init__`, `put`, `get`, `remove`. Paste your attempt and I'll check it. This is direct array indexing, O(1) for all three operations — about as good as it gets for this version of the problem (the "best" here, no need for buckets/chaining since there's no collision possible).
