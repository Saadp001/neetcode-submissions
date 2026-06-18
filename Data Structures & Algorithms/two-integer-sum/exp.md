whats the complexity and why this solution is better than two pointers
**Hashmap solution:** O(n) time — single pass, dict insert/lookup are O(1) average. O(n) space — `seen` can hold up to n entries.

**Why it beats two-pointer here:** two-pointer itself is O(n), but it only works on a sorted array. Since this problem needs you to return the *original* indices, you can't just sort `nums` directly — you'd lose the index-value mapping. You'd have to sort `(value, original_index)` pairs instead, which costs O(n log n) for the sort itself, on top of the O(n) two-pointer scan. Net result: O(n log n) time, O(n) space (still need extra space to store those pairs).

So it's not "two-pointer is bad," it's that the sorting tax this specific problem forces on you (because you need to preserve original positions) makes it strictly slower than hashmap — O(n log n) vs O(n), same O(n) space either way. Hashmap just gets you the O(n) lookup without ever needing to sort.

If this problem didn't ask for original indices and the array was *already* sorted, two-pointer would actually win — O(n) time, O(1) space, beating hashmap's O(n) space. That's the general pattern: two-pointer is great when you don't need to preserve original order/indices; hashmap is great when you do.
