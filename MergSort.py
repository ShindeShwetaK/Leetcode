############################
#Q88.Merge Sort
#https://leetcode.com/problems/merge-sorted-array/
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        last=m+n-1

        while m>0 and n>0:
            if nums1[m-1]>nums2[n-1]:
                nums1[last]=nums1[m-1]
                m-=1
            else:
                nums1[last]=nums2[n-1]
                n-=1
            last-=1

        while n>0:
            nums1[last]=nums2[n-1]
            n-=1
            last-=1
##################################################
#Q1209.remove-all-adjacent-duplicates-in-string-ii 
s = "deeedbbcccbdaa"
k = 3    
stack=[]
for c in s:
    if stack and stack[-1][0]==c:
        stack[-1][1]+=1
    else:
        stack.append([c,1])
    if stack[-1][1]==k:
        stack.pop()            
res=""
for char,count in stack:
    res+=(char*count)
print(res)
#################################################

        
