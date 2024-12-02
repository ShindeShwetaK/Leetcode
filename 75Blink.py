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

###################################################################
#Q2. Find Greatest Substring.

def gcdOfStrings(self, str1: str, str2: str) -> str:
    def gdc(a ,b):
        while b:
            a , b = b , a % b
        return a
    return str1([ :gcd(len(str1), len(str2) ]) if str 2 +str1 == str1 + str2 else ''

####################################################################
#Q3. Extra Candies

    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        candies_status = []
        max_candy = max(candies)

        for i in range(len(candies)):
           count = candies[i] + extraCandies
           if count >= max_candy:
              candies_status.append(True)
           else:
              candies_status.append(False)

        return candies_status

###################################################################

        
    

