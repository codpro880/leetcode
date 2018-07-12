"""
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.
"""
class Solution:
    def groupAnagrams(self, strs):
        anagrams = []
        results = []
        for string in strs:
            anagram = self.create_anagram(string)
            if anagram in anagrams:
                ind = anagrams.index(anagram)
                results[ind].append(string)
            else:
                anagrams.append(anagram)
                results.append([string])

        return results

    def create_anagram(self, string):
        result = {}
        for char in string:
            if char in result:
                result[char] += 1
            else:
                result[char] = 0
        return result

if __name__ == "__main__":
    sol = Solution()
    input = ["eat", "tea", "tan", "ate", "nat", "bat"]
    output = sol.groupAnagrams(input)
    print(output)
