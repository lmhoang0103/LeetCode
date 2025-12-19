


heapq.heapify(list) — Transform list into min-heap in-place, O(n).
heapq.heappush(heap, item) — Push item, maintain min-heap, O(log n).
heapq.heappop(heap) — Pop and return smallest item, O(log n).
heapq.heappushpop(heap, item) — Push item then pop smallest (more efficient than separate calls).
heapq.heapreplace(heap, item) — Pop smallest then push item (returns popped value).
heapq.merge(*iterables, key=None, reverse=False) — Merge multiple sorted inputs into sorted iterator.
heapq.nlargest(k, iterable, key=None) — Return k largest elements.
heapq.nsmallest(k, iterable, key=None) — Return k smallest elements.