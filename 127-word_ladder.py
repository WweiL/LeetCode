from collections import deque
from collections import defaultdict
class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        n = len(beginWord)
        queue = deque()
        wordList = set(wordList)
        queue.append((beginWord, 1))
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        step = float('inf')
        while queue:
            word, length = queue.popleft()
            if word == endWord:
                return length
            for i in range(n):
                for c in alphabet:
                    w = word[:i] + c + word[i+1:]
                    if w in wordList:
                        # if w == endWord:
                            # return length+1
                        queue.append((w, length+1))
                        wordList.remove(w)
            
        return 0
# my solution, O(n^2) time building graph. TLE.
# class Solution:
#     def ladderLength(self, beginWord, endWord, wordList):
#         """
#         :type beginWord: str
#         :type endWord: str
#         :type wordList: List[str]
#         :rtype: int
#         """
        
#         def diff(word1, word2):
#             count = 0
#             for i in range(len(word1)):
#                 if word1[i] != word2[i]:
#                     count += 1
#             return count
        
#         def bfs(beginWord, endWord, neighbors):
#             marked = defaultdict(bool)
#             queue = deque()
#             queue.append((beginWord, 0))
#             while queue:
#                 i = queue.popleft()
#                 if i[0] == endWord:
#                     return i[1]
#                 for neighbor in neighbors[i[0]]:
#                     if not marked[neighbor]:
#                         if neighbor == endWord:
#                             return i[1]+1
#                         marked[neighbor] = True
#                         queue.append((neighbor, i[1]+1))
                    
#             return float('inf')
                        
                
#         if not endWord in wordList:
#             return 0
        
#         neighbors = defaultdict(list)
#         n = len(wordList)
#         for i in range(n):
#             for j in range(i+1, n):
#                 if diff(wordList[i], wordList[j]) == 1:
#                     neighbors[wordList[i]].append(wordList[j])
#                     neighbors[wordList[j]].append(wordList[i])
#         starter_pack = []
#         for i in wordList:
#             if diff(i, beginWord) == 1:
#                 starter_pack.append(i)
                
#         min_step = float('inf')
#         for i in starter_pack:
#             min_step = min(min_step, bfs(i, endWord, neighbors))
            
#         return min_step + 2 if min_step != float('inf') else 0
