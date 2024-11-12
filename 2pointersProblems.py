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
    def maxProfit(self, prices: List[int]) -> int:
        sum = 0
        for i in range(1,len(prices)): 
            if prices[i] > prices[i-1]:
                   sum += prices[i] - prices[i-1]
        return sum
