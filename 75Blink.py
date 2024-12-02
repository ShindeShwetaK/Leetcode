############https://leetcode.com/studyplan/leetcode-75/#################
############################Array String################################

#Q1 Merg string Alternately
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        new_string = ""
        max_len = max(len(word1), len(word2))

        for i in range(max_len):
            if i <len(word1):
                new_string += word1[i]

            if i < len(word2):
                new_string += word2[i]

        return new_string

#OR
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        new_string = []
        
        for i,j in zip(word1, word2):
            new_string.append(i)
            new_string.append(j)

        new_string.append(word1[len(word2):])
        new_string.append(word2[len(word1):])

        return "".join(new_string)

