import string

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set, queue = set(wordList), deque()
        if endWord not in word_set:
            return 0
        
        queue.append((beginWord, 1))

        while queue:
            queue_size = len(queue)

            for _ in range(queue_size):
                word, level = queue.popleft()

                for i, ch in enumerate(word):
                    for new_ch in string.ascii_lowercase:
                        if ch == new_ch:
                            continue
                        next_word = word[:i] + new_ch + word[i+1:]

                        if next_word == endWord:
                            return level + 1
                        if next_word in word_set:
                            word_set.remove(next_word)
                            queue.append((next_word, level + 1))

        return 0
        