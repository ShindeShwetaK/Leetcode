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

        

   
        






        


        






            




        
