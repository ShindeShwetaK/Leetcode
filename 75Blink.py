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
#Q4. FlowerBed Problem
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowerbed= [0]+flowerbed+[0]
        for i in range(1,len(flowerbed)-1):
            if flowerbed[i] == 0 and flowerbed[i-1] == 0  and flowerbed[i+1] == 0:
                flowerbed[i] = 1
                n =-1
        if n<=0:
            return True
        else:
            return False
#######################################################################
#Q5 Vowels interchange
 def reverseVowels(self, s: str) -> str:
        s = list(s)
        vowel = set('aeiouAEIOU')
        left , right = 0, len(s) - 1

        while left < right:
            if s[left] not in vowel:
                left += 1
            elif s[right] not in vowel:
                right -= 1
            else:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1

        return "".join(s)
        
    

