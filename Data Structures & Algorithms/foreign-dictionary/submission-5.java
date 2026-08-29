class Solution {
    public String foreignDictionary(String[] words) {
        StringBuilder res = new StringBuilder();
        var adj = new HashMap<Character, Set<Character>>();
        for(String word : words){
            for(char ch : word.toCharArray()){
                adj.put(ch, new HashSet<Character>());
            }
        }

        var indegree = new HashMap<Character, Integer>();
        for(char ch : adj.keySet()){
            indegree.put(ch, 0);
        }

        for(int i = 0; i < words.length - 1; ++i){
            String cur = words[i], nxt = words[i+1];
            int minLen = Math.min(cur.length(), nxt.length());

            if(cur.length() > nxt.length() && cur.substring(0,minLen).equals(nxt.substring(0,minLen))){
                return res.toString();
            }

            for(int j = 0; j < minLen; ++j){
                char c = cur.charAt(j), n = nxt.charAt(j);
                if(c != n){
                    if(!adj.get(c).contains(n)){
                        adj.get(c).add(n);
                        indegree.put(n, indegree.get(n) + 1);
                    }
                    break;
                }
            }
        }

        var queue = new ArrayDeque<Character>();
        for(char ch : indegree.keySet()){
            if(indegree.get(ch) == 0){
                queue.offer(ch);
            }
        }

        while(!queue.isEmpty()){
            char cur = queue.poll();
            res.append(cur);

            for(char nxt : adj.get(cur)){
                indegree.put(nxt, indegree.get(nxt) - 1);
                if(indegree.get(nxt) == 0){
                    queue.offer(nxt);
                }
            }
        }

        return res.length() == indegree.size()? res.toString() : "";
    }
}
