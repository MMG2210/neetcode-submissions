class Solution {
    public int ladderLength(String beginWord, String endWord, List<String> wordList) {
        var wordSet = new HashSet<String>(wordList);
        int res = 0;
        
        if (!wordSet.contains(endWord) || beginWord.equals(endWord)){
            return res;
        }

        var queue = new ArrayDeque<String>(List.of(beginWord));
        while(!queue.isEmpty()){
            res++;
            int queueSize = queue.size();
            for(int i = 0; i < queueSize; ++i){
                var word = queue.poll();
                if(word.equals(endWord)){
                    return res;
                }

                for(int j = 0; j < word.length(); ++j){
                    for(char ch = 'a'; ch <= 'z'; ++ch){
                        if(ch == word.charAt(j))
                            continue;
                        String nextWord = word.substring(0, j) + ch + word.substring(j+1);
                        if(wordSet.contains(nextWord)){
                            queue.add(nextWord);
                            wordSet.remove(nextWord);
                        }
                    }
                }
            }
        }

        return 0;
    }
}
