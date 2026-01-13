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

########################################################################
739. Daily Temperatures
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []

        for index, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                stack_temp, stack_index = stack.pop()
                result[stack_index] = index - stack_index

            stack.append((temp, index))

        return result

#######################################################################
503. Next Greater Element II
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        n = len(nums)
        res = [-1] * n

        for i in range(2 * n):
            curr = nums[i % n]
            while stack and nums[stack[-1]]< curr:
                res[stack.pop()] = curr
            if i < n:
                stack.append(i)

        return res

###############################################################
901. Online Stock Span
class StockSpanner:

    def __init__(self):
        self.stack =[]
        

    def next(self, price: int) -> int:
        span = 1
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack.pop()[1]
        self.stack.append((price, span))
        return span
#################################################################
853. Car Fleet
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [[p, s] for p , s in zip(position, speed)]
        st =[]
        print(sorted(cars))

        for p, s in sorted(cars)[::-1]:
            time = (target - p) / s
            print(time)
            if not st or time > st[-1]:
                st.append(time)

        return len(st)
##################################################################
402. Remove K Digits
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack =[]

        for i in num:
            while stack and stack[-1] > i and k >0:
                stack.pop()
                k -= 1
            stack.append(i)

        while k > 0:
            stack.pop()
            k -= 1

        result = "".join(stack).lstrip('0')

        return result if result else "0"
  
