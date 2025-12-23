#Q1.Sum of 2 numbers are retuen index when target found
#https://leetcode.com/problems/two-sum/
def TwoSum(nums,target):
    Index=[]
    i=0
    j=1
    y=len(nums)+1
    temp= nums[i]
    while i!=y-1:
        for x in nums[j:y]:
            temp+=x
            if temp==target:
                append.Index(i)
                append.Index(j)
                return Index
            else:
                j+=1
                temp= nums[i]
                if j+1==y:
                    i+=1
                    temp= nums[i]
                    j=i+i
#Easy solution
def twoSum(nums,target):
        n = len(nums)
        for i in range(n-1):
            for j in range(i+1, n):
                if nums[i]+nums[j] == target:
                    return [i,j]
        return []
    or

        pair_idx = {}

        for i, num in enumerate(nums):
            if target - num in pair_idx:
                return [i, pair_idx[target - num]]
            pair_idx[num] = i
###########################################################################
#Q11. Container with most water
#https://leetcode.com/problems/container-with-most-water/
    def maxArea(self, height: List[int]) -> int:
        res=0
        l,r=0,len(height)-1

        while l<r:
            area=(r-l)*min(height[l],height[r])
            res=max(res,area)

            if height[l]< height[r]:
                l+=1
            else:
                r-=1
        return res
###########################################################################
#Q5
        if len(s) <= 1:
           return s
        
        Max_Len=1
        Max_Str=s[0]
        for i in range(len(s)-1):
            for j in range(i+1,len(s)):
                if j-i+1 > Max_Len and s[i:j+1] == s[i:j+1][::-1]:
                    Max_Len = j-i+1
                    Max_Str = s[i:j+1]

        return Max_Str
#####################################################################
#Q15.3Sum
#https://leetcode.com/problems/3sum/description/
nums = [-1,0,1,2,-1,-4]
new=[]
nums.sort()
for i , a in enumerate(nums):
    if i >0 and a==nums[i-1]:
        continue
        
    l,r=i+1, len(nums)-1
    while l<r:
        threesum= a+nums[l]+nums[r]
        if threesum>0:
            r-=1
        elif threesum<0:
            l+=1
        else:
            new.append([a,nums[l],nums[r]])
            l+=1
            while nums[l]==nums[l-1] and l<r:
                l+=1
print(new)
#sort=o(nlogn)+o(n^2) this is complete o(n^2) as it has 2 loops
#######################################################################################
#Q18.4Sum
#https://leetcode.com/problems/4sum/
        new=[]
        nums.sort()
        for i in range(len(nums)-3):
            if i >0 and nums[i]==nums[i-1]:
                continue       
            for j in range(i+1,len(nums)-2):
                if j >i+1 and nums[j]==nums[j-1]:
                   continue
                
                l,r=j+1, len(nums)-1
                while l<r:
                   foursum= nums[i]+nums[j]+nums[l]+nums[r]
                   if foursum>target:
                       r-=1
                   elif foursum<target:
                       l+=1
                   else:
                       new.append([nums[i],nums[j],nums[l],nums[r]])
                       while l<r and nums[l]==nums[l+1]:
                          l+=1
                       while l<r and nums[r]==nums[r-1]:
                          r-=1
                       l+=1
                       r-=1
        return new
################################################################
#Rob the house
        prev_rob = max_rob = 0

        for curr_val in nums:
            temp = max(max_rob, prev_rob + curr_val)
            prev_rob = max_rob
            max_rob = temp

        return max_rob
####################################################################################
#Q75 Sorting the colors in place

        l, r = 0, len(nums)
        while l <= r - 1:  
            for i in range(l+1, r):
                if nums[i] < nums[l]:
                    nums[l], nums[i] = nums[i], nums[l]
            l+=1
            #or
            nums[:] = [0]*nums.count(0)+[1]*nums.count(1)+[2]*nums.count(2)
            #o(n^2) time space o(1)
######################################################################################
#Q80. remmove duplicate from sorted array II
#https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/description/
                        l,r=0,1
                        count=0
                        while r<len(nums):
                            if nums[l]==nums[r]:
                                count+=1
                                if nums[l]==nums[r] and count>=2:
                                    nums.remove(nums[r])
                                    continue
                            else:
                                count=0
                            l+=1
                            r+=1
                        return len(nums)
######################################################################################
#q83. Remove duplicated from listed list
#https://leetcode.com/problems/remove-duplicates-from-sorted-list/
            cur=head
            while cur:
                while cur.next and cur.next.val==cur.val:
                    cur.next=cur.next.next
                cur=cur.next
            return head
#######################################################################################
#q82 Remove duplicate from LL II
#https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/description/
        fake = ListNode(-1)
        fake.next = head
        curr, prev = head, fake
        while curr:
            while curr.next and curr.val == curr.next.val:
                curr = curr.next
            if prev.next == curr:
                prev = prev.next
                curr = curr.next
            else:
                prev.next = curr.next
                curr = prev.next
        return fake.next
#######################################################################################
#Q.167.Two sum II with sorted array
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l,r=0,len(numbers)-1
        while l < r :
            cursum=numbers[l]+numbers[r]
            if cursum > target :
                r-=1
            elif cursum < target :
                l+=1
            else:
                return [l+1,r+1]
        return []
######################################################################################
#Q259.3sum smaller
    n=[-2,0,1,3]
    n.sort()
    target=2
    c=0
    l,r=1,len(n)-1
    for i in range(len(n)):
     while l<r:
        three=n[i]+n[l]+n[r]
         if three >= target:
            r-=1
        else:
            c+=r-1
            l+=1
print(c)
#######################################################################################
#Q283. Move zeros
#https://leetcode.com/problems/move-zeroes/description/
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l=0
        for r in range(len(nums)):
            if nums[r]:
                nums[l],nums[r]=nums[r],nums[l]
                l+=1
        return nums
#o(1) as we have note used any memory for swaping we are swaping within
####################################################################################
#Q763.Partitation Lables
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
            lastindex={}
            for i , a in enumerate(s):
                lastindex[a]=i
            
            result=[]
            size,end=0,0
            for i , a in enumerate(s):
                size+=1
                end=max(end,lastindex[a])
                if i==end:
                    result.append(size)
                    size=0
            return result
#######################################################################################
#remove duplicate @26
    def removeDuplicates(self, nums: List[int]) -> int:
        new_array=[]
        seen=set()
        
        for i in nums:
            if i not in seen:
                new_array.append(i)
                seen.add(i)


#######################################################################################
#buy and sell problem Q122
        max_profit = 0
        min_profit = float('inf')

        for i in prices:
            if i < min_profit:
                min_profit = i
            
            profit = i - min_profit

            if profit > max_profit:
                max_profit = profit

        return max_profit

#########################################################################
#Q 283 Move the zeros
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0

        for right in range(len(nums)):
            if nums[right] !=0 :
                nums[right] , nums[left] = nums[left], nums[right]
                left +=1

#######################################################################
#Q392 IS subsequence
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sc = tc = 0

        while sc < len(s) and tc < len(t):
            if s[sc] == t[tc]:
                sc += 1
            tc += 1


        return sc == len(s)
###################################################################
#Q1679 max Num of sum k
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        l, r = 0, len(nums)-1
        sum_num = 0
        counter = 0   
        
        while l<r:   
            sum_num = nums[l] + nums[r]
            if sum_num == k:
                counter += 1
                l += 1
                r -= 1
            elif sum_num < k:
                l += 1
            else:
                r -= 1

        return counter 

############################################################
#Q88 Merging 2 array
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i , j , k = m - 1, n - 1, m + n - 1

        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -=1
            k -= 1
        
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1
or 
        i, j, k = m - 1, n - 1, m + n - 1

        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            
            k -= 1
################################################################
#209. Minimum Size Subarray Sum
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        cursum = 0
        result = len(nums) + 1


        for r, n in enumerate(nums):
            cursum += n
            while cursum >=target:
                result = min(result, r-l+1)
                cursum -= nums[l]
                l += 1

       return res % (len(nums) +1)
##################################################################
#290 Word Pattern
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pattern = list(pattern)
        s=s.split()
        word = {}

        if len(pattern) != len(s):
            return False

       if len(set(pattern)) != len(set(s)):
           return False

       for i in range(len(s)):
           if s[i] not in words:
               words[s[i]] = pattern[i]
           else:
               if words[s[i]] != pattern[i]:
                   return False

       return True
#######################################################
#Q242. Valid Anagram
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False

        ##list1 = ''.join(sorted(s))
        ##list2 = ''.join(sorted(t))

        #for i in range(len(s)):
           # list1.append(s[i])
        #list1.sort()
        
       # list2 = []
       # for i in range(len(t)):
            #list2.append(t[i])
        #list2.sort()

        ##return list1 == list2

        counter = {}

        for i in range(len(s)):
            if s[i] not in counter:
                counter[s[i]] = 1
            else:
                counter[s[i]] += 1

        for i in range(len(t)):
            if t[i] not in counter or counter[t[i]] <= 0:
                return False
            counter[t[i]] -= 1

        return True
########################################################
125. Valid Palindrome
ss = "".join(c.lower() for c in s if c.isalnum())

l = 0
r = len(ss) -1

while l < r:
    if ss[l] == ss[r]:
        l += 1
        r -= 1
    else:
        return False
return True

#######################################################
344. reverse string
        l = 0
        r = len(s) - 1

        while l < r:
            s[r] , s[l] = s[l], s[r]
            l += 1
            r -= 1
######################################################
977. Square root or sorted array
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        left = 0
        right = len(nums) - 1

        for i in range(len(nums) - 1, -1, -1):
            if  abs(nums[left]) > abs(nums[right]):
                res[i] = nums[left] ** 2
                left += 1
            else:
                res[i] = nums[right] ** 2
                right -= 1

        return res
##########################################################
16 3 sum closest
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        sums = nums[0] + nums[1] + nums[2]
        nums.sort()


        for i in range(len(nums) - 2):

            j = i + 1
            k = len(nums) - 1

            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if abs(total - target) < abs(sums - target):
                    sums = total
                if total > target:
                    k -= 1
                elif total < target:
                    j += 1
                else:
                    break
         
        return sums










