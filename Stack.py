496. Next Greater Element I

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        dict_num = {}

        for num in nums2:
            while stack and num > stack[-1]:
              dict_num[stack.pop()] = num 

            stack.append(num)

        for nums in stack:
            dict_num[nums] = -1

        return [dict_num[nums] for nums in nums1]


####################################################################
682. Baseball Game
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack =[]

        for i in operations:
            if i == "+" :
                stack.append(stack[-1] + stack[-2])

            elif i == "D":
                stack.append(stack[-1] * 2)
              
            elif i == "C":
                stack.pop()
            else:
                stack.append(int(i))

        return(sum(stack))

  ##################################################
1081. Smallest Subsequence of Distinct Characters
316. Remove Duplicate Letters
class Solution:
    def smallestSubsequence(self, s: str) -> str:
        unique = set()
        stack = []

        last_occur = {char : i for i , char in enumerate(s)}

        for i, char in enumerate(s):
            if char in unique:
                continue

            while stack and char <  stack[-1] and i < last_occur[stack[-1]]:
                 unique.remove(stack.pop())
                ##stack.pop()

                
            unique.add(char)
            stack.append(char)
            print( stack, last_occur)

        return "".join(stack)
        #############################################################
1475. Final price with special discount
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack =[]

        for i , cur in enumerate(prices):
            while stack and prices[stack[-1]] >= cur:
                prices[stack.pop()] -= cur

            stack.append(i)

        return prices
  
