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





            




        
