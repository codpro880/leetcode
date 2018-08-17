"""
Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
Note:

Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output: 5

Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.
Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: 0

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
"""
def ladder_len(beg_word, end_word, word_list):
    return ladder_len_helper(beg_word, end_word, word_list, 1)

def ladder_len_helper(beg_word, end_word, word_list, length):
    if beg_word == end_word:
        return length
    if not word_list:
        return 0
    words_to_visit = []
    for w in word_list:
        if can_reach(w, beg_word):
            words_to_visit.append(w)
    if not words_to_visit:
        return 0
    l = word_list[:]
    l.remove(words_to_visit[0])
    min_length = ladder_len_helper(words_to_visit[0], end_word, l, length+1)
    for w in words_to_visit[1:]:
        l = word_list[:]
        l.remove(w)
        cur_len = ladder_len_helper(w, end_word, l, length+1)
        if min_length == 0:
            min_length = cur_len
        if cur_len != 0:
            min_length = min(cur_len, min_length)
    return min_length

def can_reach(w, beg_word):
    diffs = [w_char == beg_char for w_char, beg_char in zip(w, beg_word)]
    return diffs.count(False) == 1
                         

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        return ladder_len(beginWord, endWord, wordList)

if __name__ == "__main__":
    sol = Solution()

    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","dot","dog","lot","log","cog"]
    print(sol.ladderLength(beginWord, endWord, wordList))

    beginWord = "test"
    endWord = "sext"
    wordList = ["rest", "best", "nest", "next", "sext"]
    print(sol.ladderLength(beginWord, endWord, wordList))
