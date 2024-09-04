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
        
