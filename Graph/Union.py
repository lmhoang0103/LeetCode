class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        # Stones are connected if share row or col
        # In each connected components size k => can remove k-1 stones
        # For each components, can keep one stone => Keep len(Components) stone
        # Max remove = total_stones - number of components

        # For each node, parent[nodeI] = k
        # For parent node: parent[i]  = i
        parent = {}

        def find(x):
            if x not in parent:
                parent[x] = x
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            rx, ry = find(x), find(y)
            if rx != ry:
                parent[ry] = rx

        OFFSET = 10001  # bigger than max coordinate

        for r, c in stones:
            union(r, c + OFFSET)

        roots = set()
        for r, _ in stones:
            roots.add(find(r))

        return len(stones) - len(roots)
        