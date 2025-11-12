from collections import defaultdict, deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_list = set(wordList)
        if endWord not in word_list:
            return 0
        
        adj_list = defaultdict(list)

        word_len = len(beginWord)

        for word in word_list:
            for i in range(word_len):
                pattern = word[:i]+'*'+word[i+1:]
                adj_list[pattern].append(word)

        queue = deque([(beginWord,1)])
        vigited = set()
        vigited.add(beginWord)

        while queue:
            curr, lv = queue.popleft()

            for i in range(word_len):
                pattern = curr[:i]+"*"+curr[i+1:]

                for word in adj_list[pattern]:
                    if word == endWord:
                        return lv+1
                    if word not in vigited:
                        vigited.add(word)
                        queue.append((word,lv+1))

                adj_list[pattern] = []

        return 0
