class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        for src, dst in sorted(tickets)[::-1]:
            adj[src].append(dst)
        
        stack, res = ["JFK"], []

        while stack:
            cur = stack[-1]
            if not adj[cur]:
                res.append(stack.pop())
            else:
                stack.append(adj[cur].pop())
        
        return res[::-1]
