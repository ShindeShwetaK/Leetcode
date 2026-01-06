904. Fruit Into Baskets
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        unique = {}
        l = 0
        max_len = 0

        for r, n in enumerate(fruits):
            if n not in unique:
                unique[n] = 1
            else:
                unique[n] += 1


            while len(unique) > 2:
                unique[fruits[l]] -= 1
                if unique[fruits[l]] == 0:
                    del unique[fruits[l]]
                l += 1

            max_len = max(max_len, r - l + 1)


        return max_len

------------------------------------------------------------------
713. Subarray Product Less Than K
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if  k <= 1:
            return 0

        l = 0
        max_nums = 0
        curr_mul = 1

        for r in range(len(nums)):
            curr_mul *= nums[r]

            while curr_mul >= k:
                curr_mul //= nums[l]
                l += 1

            max_nums += r - l + 1

        return max_nums

-----------------------------------------------
## Prefix Subarray
303. Range Sum Query - Immutable

class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        

    def sumRange(self, left: int, right: int) -> int:
        return sum(self.nums[left:right + 1])
--------------------------------------------------------------
724. Find Pivot Index
#Fast
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        pre_sum = sum(nums)
        post_sum = 0

        for i, n in enumerate(nums):
            pre_sum -= n

            if pre_sum == post_sum:
                return i

            post_sum += n

        return -1

or 
#slow
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if sum(nums[:i]) == sum(nums[i+1:]):
                return i

        return -1

-------------------------------------------------
2574. Left and Right Sum Differences
class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        left_sum = [0] * len(nums)
        right_sum = [0] * len(nums)
        sum_l = 0
        sum_r = 0
        final =[]

        for i in range(1,len(nums)):
            sum_l += nums[i-1]
            left_sum[i] = sum_l

        for i in range(len(nums)- 2, -1, -1):
            sum_r += nums[i+1]
            right_sum[i] = sum_r

        for i in range(len(nums)):
            final.append(abs(left_sum[i] - right_sum[i]))

        return final

class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        pre = sum(nums)
        res = [0] * len(nums)
        post = 0

        for i in range(len(nums)):
            pre -= nums[i]
            res[i] = abs(post -pre)
            post += nums[i]

        return res

------------------------------------------------------------------
974. Subarray Sums Divisible by K
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = 0
        sums = 0
        feq = {0:1}

        for x in nums:
            sums += x
            r = sums % k
            count += feq.get(r, 0)
            feq[r] = feq.get(r , 0) + 1

        return count

----------------------------------------------------
523. Continuous Subarray Sum
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainder_dict = {0: -1}  # Initializing with 0 to handle cases where the subarray itself is a multiple of k
        cum_sum = 0
        
        for i in range(len(nums)):
            cum_sum += nums[i]
            remainder = cum_sum % k
            
            if remainder in remainder_dict:
                if i - remainder_dict[remainder] > 1:  # Ensure the subarray length is at least 2
                    return True
            else:
                remainder_dict[remainder] = i
        
        return False

####################################################
Line Sweep
253 Meeting roon II
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        nums_rooms = 0
        ans = -1

        times = []
        for i in intervals:
            times.append((i[0], 1))
            times.append((i[1], -1))

        times.sort()

        for i in times:
            nums_rooms += i[1]
            ans = max(ans, nums_rooms)

        return ans

-------------------------------------------------------------
252. Meeting room I
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key = lambda x: x[0])
        for i in range(len(intervals) - 1):
            if intervals[i][1] > intervals[i + 1][0]:
                return False
        return True

---------------------------------------------------------------
2406. Divide Intervals Into Minimum Number of Groups
class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:

        times = []
        count = 0
        final = 0

        for i in intervals:
            times.append((i[0], 1))
            times.append((i[1], -1))

        times.sort(key = lambda x: (x[0], -x[1]))

        for t in times:
            count += t[1]
            final = max(final, count)

        return final
-----------------------------------------------------
#1109. Corporate flight booking
        booking_seat = [0] * (n + 1)

        for f, l , s in bookings:
            booking_seat[f - 1] += s
            booking_seat[l] -= s

        for i in range(1, n):
            booking_seat[i] += booking_seat[i - 1]

        return booking_seat[:n]

------------------------------------------------------
#5.	1854. Maximum Population Year
class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        event = []
        
        for b,  d in logs:
            event.append((b, 1))
            event.append((d, -1))

        event.sort()

        max_pop = 0
        pop = 0
        best_year = 0

        for year, change in event:
            pop += change
            if pop > max_pop:
                max_pop = pop
                best_year = year

        return best_year








        



            

            

            
        
