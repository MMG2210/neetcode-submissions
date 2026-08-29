class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {ch : set() for word in words for ch in word}
        indegree = {ch : 0 for ch in adj}
        res = ""

        for i in range(len(words) - 1):
            cur, nxt = words[i], words[i+1]
            min_len = min(len(cur), len(nxt))
            if len(cur) > len(nxt) and cur[:min_len] == nxt[:min_len]:
                return res
            
            for j in range(min_len):
                if cur[j] != nxt[j]:
                    if nxt[j] not in adj[cur[j]]:
                        adj[cur[j]].add(nxt[j])
                        indegree[nxt[j]] += 1
                    break
        
        queue = deque([ch for ch in indegree if indegree[ch] == 0])

        while queue:
            cur = queue.popleft()
            res += cur

            for nxt in adj[cur]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    queue.append(nxt)
        
        return res if len(res) == len(indegree) else ""
