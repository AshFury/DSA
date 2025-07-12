# Last updated: 12/07/2025, 18:25:49
class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        word=str()
        length=max(len(word1),len(word2))
        for i in range(length):
            if i<len(word1):
                word += word1[i]
            if i<len(word2):
                word += word2[i]
        return word
            
        