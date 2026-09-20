#1249. Minimum Remove to Make Valid Parentheses
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        total_open = 0
        bal = 0
        char_list = []
        result = []

        for i in s:
            if i == "(":
                total_open += 1
                bal += 1

            elif i == ")":
                if bal == 0:
                    continue
                bal -= 1

            char_list.append(i)

        open_to_keep = total_open - bal

        for i in char_list:
            if i == "(":
                open_to_keep -= 1
                if open_to_keep < 0:
                    continue
            result.append(i)

        return "".join(result)

--------------------------------------------------------

973. K Closest Points to Origin

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance = {}
        for i, num in enumerate(points):
            dist = ((num[0])**2+(num[1]**2))
            distance[i] = dist

        final = heapq.nsmallest(k, distance.items(), key = lambda x:x[1])
        return [point[i] for i, _ in final]

-----------------------------------------------------------------------------
56. Merge Intervals

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merged = []
        intervals.sort()
        prev = intervals[0]

        for i in range(1, len(intervals)):
            if prev[1] >= intervals[i][0]:
                prev[1] = max(intervals[i][1], prev[1])

            else:
                merged.append(prev)
                prev = intervals[i]

        merged.append(prev)
        return merged

-------------------------------------------------------------
560. Subarray Sum Equals K

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        feq = {0:1}
        prefix =0 

        for i in nums:
            prefix += i
            if prefix -k  in feq:
                count += feq[prefix -k]
            if prefix in feq:
                feq[prefix] += 1
            else:
                feq[prefix] = 1

        return count

-----------------------------------------------------------------
77. Combinations

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        subset = []


        def createcombo(i):
            if len(subset) == k:
                result.append(subset[:])
                return 

            for num in range(i, n + 1):
                subset.append(num)
                createcombo(num + 1)
                subset.pop()

        createcombo(1)
        return result

________________________________________________________________________
39. Combination Sum
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def make_combo(idx, comb, total):
            if target == total:
                result.append(comb[:])
                return

            if total > target or idx >= len(candidates):
                return

            comb.append(candidates[idx])
            make_combo(idx, comb, total + candidates[idx] )
            comb.pop()
            make_combo(idx + 1, comb, total)

            return result



        return make_combo(0, [], 0)

_________________________________________________________________________
40. Combination Sum II

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []

        def dfs(target, start, comb):
            if target < 0:
                return

            if target == 0:
                result.append(comb)
                return

            for i in range(start,len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                if candidates[i] > target:
                    break
                dfs(target - candidates[i] ,  i + 1, comb + [candidates[i]]) 



        dfs(target, 0 , [])
        return result
_______________________________________________________________
131. Palindrome Partitioning
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_palindrome(sub):
            return sub == sub[::-1]

        def backtrack(start, path):
            if start == len(s):
                result.append(path[:])
                return
            for end in range(start + 1, len(s) + 1):
                if is_palindrome(s[start:end]):
                    backtrack(end, path + [s[start:end]])

        result = []
        backtrack(0, [])
        return result

______________________________________________________________________
Letter combination of the phone number

class Solution:
     def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        digit_to_letters = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }

        def backtrack(idx, comb):
            if idx == len(digits):
                res.append(comb[:])
                return
            
            for letter in digit_to_letters[digits[idx]]:
                print(digit_to_letters[digits[idx]],digits[idx],  comb + letter, idx)
                backtrack(idx + 1, comb + letter)

        res = []
        backtrack(0, "")

        return res

__________________________________________________
128. Longest Consecutive Sequence
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0

        for n in num_set:
            if  n - 1 not in num_set:
                length = 1

                while n + length in num_set:
                    length += 1

                longest = max(longest, length)

        return longest

______________________________________________
160. Intersection of Two Linked Lists
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        lista = headA
        listb = headB

        while lista != listb:
            lista = lista.next if lista else headB
            listb = listb.next if listb else headA

        return listb

__________________________________________________
def another_one(digits):
	carry = 0
	result = []
	length = len(digits) - 1
	j = length
	
	while j >= 0:
	  total= 0
	  total += carry
	  
	  if j == length:
	     total = digits[j] + 1
	  else:
	     total += digits[j]
	     
	  num = total % 10
	  carry = total // 10
	  result.append(num)
	  j -= 1
	  
	  
	if carry:
	  result.append(carry)
	  
	return result[::-1]

____________________________________________________
def weakest_strong_link(strength ):
	
	
	for i in range(len(strength)):
	  for j in range(len(strength[0])):
	    min_number = min(strength[i])
	    max_number = max(cols[j] for cols in strength)
	    if strength[i][j] == min_number and strength[i][j] == max_number:
	      return strength [i][j]
	      
	return -1

___________________________________________________________
def triangular_sum(nums):
  n = len(nums)
  j = 0
  
  while n >= 0:
    for i in range(len(nums) - (j+ 1)):
      nums[i] = (nums[i] + nums[i+1]) % 10
  
    n -= 1
    j += 1
  return nums[0]


    def triangular_sum(nums):
        while len(nums)>1:
            next_nums = []
            for i in range(1,len(nums)):
                next_nums.append((nums[i-1]+nums[i])%10)
            nums = next_nums
        return nums[0]


___________________________________________________
def romanToInt(s):
    roman_dict = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }

    result = 0
    for i in range(len(s)):               
        # if a next char exists AND current value < next value → subtract
        if i + 1 < len(s) and roman_dict[s[i]] < roman_dict[s[i + 1]]:
            result -= roman_dict[s[i]]
        else:
            result += roman_dict[s[i]]  
            
    return result


____________________________________________________
def min_amplitude(arr):
	if len(arr) < 5:
	  return 0
	  
	  
	arr.sort()
	
	case_1 = arr[-1] - arr[3]
	case_2 = arr[-2] - arr[2]
	case_3 = arr[-3] - arr[1]
	case_4 = arr[-4] - arr[0]
	
	
	return min(case_1, case_2, case_3, case_4)
	
	
	  
        

   
        __________________________________________________________
	def k_radius_avg(nums, k):
    n = len(nums)
    result = [-1] * n
    window_size = 2 * k + 1

    if window_size > n:          # no window fits at all
        return result

    window = sum(nums[:window_size])   # first window: indices 0 .. 2k
    result[k] = window // window_size  # its center is index k

    for i in range(k + 1, n - k):      # remaining centers
        window += nums[i + k] - nums[i - k - 1]   # add incoming, drop outgoing
        result[i] = window // window_size
    return result






        


        






            




        
