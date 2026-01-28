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

##################################################################
456. 132 Pattern
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        s2 = float('-inf')

        for i in range(len(nums) -1, -1, -1):
            if nums[i] < s2:
                return True

            while stack and nums[i] > stack[-1]:
                s2 = stack.pop()

            stack.append(nums[i])

        return False

####################################################################
907. Sum of Subarray Minimums
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        stack = []
        res = [0] *len(arr)

        for i in range(len(arr)):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()

            j = stack[-1] if stack else -1

            res[i] = res[j] + (i - j) * arr[i]
        

            stack.append(i)

        return sum(res) % (10**9+7)

########################################################################
1047 Remove All Adjacent Duplicates In String
class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []

        for char in s:
            if stack and stack[-1] == char:
                stack.pop()
            else:
                stack.append(char)

        return "".join(stack)

###############################################################
150. evaluate reverse polish notation
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in tokens:
            if i == '+':
                stack.append(stack.pop() + stack.pop())
               
            elif i == '*':
                stack.append(stack.pop() * stack.pop())
        
            elif i == "/":
               second, first = stack.pop(), stack.pop()
               stack.append(int(first / second))

            elif i == '-':
                second, first = stack.pop(), stack.pop()
                stack.append(first - second)

            else:
                stack.append(int(i))        

        return stack[0]

###############################################################
227, basic calcularor
class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num = 0
        ope = '+'

        for i , char in enumerate(s):
            if char.isnumeric():
                num = num *10 + int(char)

            if char in '+-*/' or i == len(s) -1:
                if ope == '+':
                    stack.append(num)
                elif ope == '-':
                    stack.append(-num)
                elif ope  == '*':
                    j = stack.pop() * num
                    stack.append(j)
                elif ope  == '/':
                    j = int(stack.pop() / num)
                    stack.append(j)

                ope = char
                num = 0

        return sum(stack)

######################################################
1598. Crawler Log 
class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []

        for i in logs:
            if i == './':
                continue
            elif i == '../' and stack:
                stack.pop()
            elif i!="../":
                stack.append(i)

        return len(stack)

###################################################
1021. Remove Outermost
class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack = []
        c = 0
        for i in s:
            if i == '(':
                if c > 0:
                    stack.append(i)
                c += 1

            else:
                c -= 1
                if c > 0:
                    stack.append(i)

        return "".join(stack)

###############################################################################
189. rotate array
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #while k != 0:
           # nums.insert(0, nums[-1])
            #nums.pop(-1)
           # k -= 1
        n = len(nums)
        k = k % n
        if k == 0: return
        
        print(k, nums[-k:],nums[:-k], nums[k:] )
        #3 [5, 6, 7] [1, 2, 3, 4] [4, 5, 6, 7]
        temp = nums[-k:]
        nums[k:] = nums[:-k]
        nums[:k] = temp

                

        

                

        

                
    

  
