class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj_list = {c: set() for w in words for c in w}
        indegree = {c: 0 for c in adj_list}

        for i in range(len(words) - 1):
            cur, nxt = words[i], words[i+1]
            j, min_len = 0, min(len(cur), len(nxt))
            
            if len(cur) > len(nxt) and cur[:min_len] == nxt[:min_len]:
                return ""
            
            for j in range(min_len):
                if cur[j] != nxt[j]:
                    if nxt[j] not in adj_list[cur[j]]:
                        adj_list[cur[j]].add(nxt[j])
                        indegree[nxt[j]] += 1
                    break
        
        queue = deque([c for c in indegree if indegree[c] == 0])
        res = ""

        while queue:
            print(queue)
            cur = queue.popleft()
            res += cur

            for nxt in adj_list[cur]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    queue.append(nxt)

        return res if len(res) == len(indegree) else ""