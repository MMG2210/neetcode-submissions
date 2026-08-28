class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set, res = set(wordList), 0

        if endWord not in word_set or beginWord == endWord:
            return res

        queue = deque([beginWord])

        while queue:
            res += 1

            for _ in range(len(queue)):
                word = queue.popleft()
                if word == endWord:
                    return res
                
                for i in range(len(word)):
                    for c in range(97,123):
                        if chr(c) == word[i]:
                            continue
                        next_word = word[:i] + chr(c) + word[i+1:]

                        if next_word in word_set:
                            queue.append(next_word)
                            word_set.remove(next_word)

        return 0