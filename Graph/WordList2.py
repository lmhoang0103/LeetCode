class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        # Same as WordLadder I, but we must store the path
        # This is correct, but memory limit exceeded
        if endWord not in wordList:
            return []
        l = len(beginWord)
        if len(endWord) != l:
            return []
        # How to trace back?
        # instead of store the level in the queue, we store the transformation
        patterns = defaultdict(list)
        for word in wordList:
            if len(word) != l:
                continue
            for i in range(l):
                pat = word[:i] + '*' + word[i+1:]
                patterns[pat].append(word)
        # Using a queue, store the path

        q = deque([[beginWord]])
        visited = set([beginWord])

        res = []
        found = False
        while q and not found:
            # Pop all what is in Q BFS => all that found at this step is on the same level
            tempVisited=set()
            tempPat = []
            for _ in range(len(q)):
                seq = q.popleft()
                word = seq[-1]
                if word == endWord:
                    res.append(seq)
                    found = True
                    continue
                #See what word can be turn on from this step
                #Can still remove, for if the below step reach this word => the ans will be at lower level
                for i in range(l):
                    pat = word[:i] + '*' + word[i+1:]
                    for nei in patterns[pat]:
                        if nei not in visited:
                            tempVisited.add(nei)
                            q.append(seq+ [nei])
                    tempPat.append(pat)

            visited |= tempVisited
            for pat in tempPat:
                patterns[pat] = []


        return res