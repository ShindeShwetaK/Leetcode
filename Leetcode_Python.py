#My Solution
#Question 1##########################################################################################################################
#Sum of 2 numbers are retuen index when target found
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

####################################################################################
#Q2:-Add the 2 numbers in link list
#below solution will not work on Liskedlist but will work on List
#https://leetcode.com/problems/add-two-numbers/
def addnumbers(l1,l2):
        l1new=[str(x) for x in l1]
        Conl1="".join(l1new)
        print(Conl1)
        l2new=[str(x) for x in l2]
        Conl2="".join(l2new)
        print(Conl2)
        intConl1=int(Conl1)
        intConl2=int(Conl2)
        Final=intConl1+intConl2
        Add_list= [int(x) for x in str(Final)]
        Final_list=Add_list[::-1]
        print(Final_list)
        return(Final_list)

L1=[9,9,9,9,9,9,9]
print(type(L1))
L2=[9,9,9,9]
print(addnumbers(L1,L2))
###################################################################################

#Question 9: is Palandrom or not
#Solution without converting to string
#https://leetcode.com/problems/palindrome-number/
def isPalindrome(x):
        """
        :type x: int
        :rtype: bool
        """
        x1=x
        if x1>=0:
            Reverse=0
            digit=0
            while x1!=0:
                digit=x1 % 10
                Reverse=Reverse*10+digit
                x1//=10
            if x==Reverse:
                #print(True)
                return(True)
            else:
                #print(False)
                return(False)
        else:
            return(False)

  #Palandrom solev using str
def isPalindromestr(x):
    if str(x)==str(x)[::-1]:
        return True
    else:
        return False

######################################################################
#Q13.Roman to Integer
#https://leetcode.com/problems/roman-to-integer/
def romanToInt1(s):
    mapping={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    s=s.replace('IV','IIII').replace('IX','VIIII').replace('XL','XXXX').replace('XC','LXXXX').replace('CD','CCCC').replace('CM','DCCCC')
    ans=0
    for c in s:
        ans+=mapping[c]
    return ans
  ##################################################################
  #Q14.Longest common prefix
  #https://leetcode.com/problems/longest-common-prefix/
  strs=["fliower","fliow","flight","flhdgh","flisjbcjb",'liflifli']


if len(strs) == 0:
        print("") 
res = ''
strs = sorted(strs)
print(strs)
for i in strs[0]:
    print(i)
    if strs[-1].startswith(res+i):
        print(strs[-1].startswith(res+i),res+i)
        res += i
        print(res)
    else:
         break
    print (res)
  ##############################################################
  #Q20.Validate paranthesis
  #https://leetcode.com/problems/valid-parentheses/description/
  class Solution:
    def isValid(self, s: str) -> bool:
       stack = []
       for char in s:
          if char in ["(", "{", "["]:
            stack.append(char)
          else:
             if not stack:
                return False
             current_char=stack.pop()
             if current_char == '(':
                if char != ')':
                    return False
             if current_char == '{':
                if char != '}':
                    return False
             if current_char == '[':
                if char != ']':
                    return False
       if stack:
           return False
       else:
           return True
#####################################################################
#Q49.Group Anagrams
#https://leetcode.com/problems/group-anagrams/
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_map=defaultdict(list)
        result=[]

        for s in strs:
         sorted_s=tuple(sorted(s))
         anagrams_map[sorted_s].append(s)

#####################################################################
#Q26.Remove dulipcates from a sorted list
#https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
    def removeDuplicates(self, nums: List[int]) -> int:
         new=set(nums)
         nums.clear()
         for i in new:
            nums.append(i)
         nums.sort()
         return len(nums)
      #OR
		nums[:] = sorted(set(nums))
		return len(nums)
##################################################################
#Q27.Remove elements
#https://leetcode.com/problems/remove-element/solutions/5313095/python-codes-beating-90-of-solutions-easiest-solution/
                while val in nums:
                     nums.remove(val)
                return (len(nums))
##################################################################
#Q28.Find the index of the 1st occurance
#https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/
        new = haystack.replace(needle,'A')
        if (new == haystack): return -1
        else: return new.index('A')
		#OR
        result=haystack.find(needle)
        return result
##################################################################
#Q35.Search Insrt position
def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        elif target<nums[0]: return 0
        elif target > nums[-1]:
            return nums.index(nums[-1])+1
        else:   
            for i in range(len(nums)):
                 if target<=nums[i]:
                     return i
			#or
        for i in range(len(nums)):
                 if target<=nums[i]:
                     return i
        return(len(nums))
#######################################################################     
#Q58.Length of Last Word
    def lengthOfLastWord(self, s: str) -> int:
        lis = list(s.split())
        return (len(lis[-1]))
#######################################################################
#66.Plus 1
        new=""
        new_l=[]
        for i in digits:
           new+=str(i)
        new=int(new)+1
        for i in str(new):
           new_l.append(int(i))
        return new_l
     #or
        concat=int("".join([str(i) for i in digits]))
        new=concat+1
        l= [int(i) for i in str(new)] #or l = list(map(int, str(new)))
        print(l)
#####################################################################
#Q67.Add Binary
        bin_a= int(a,2) #binary to number
        bin_b= int(b,2) #binary to number
        new_num=bin_a+bin_b
        a_b=(bin(new_num)[2:]) #number to binary
        return a_b
	    #or
	return bin(int(a,2)+int(b,2))[2:]
	    #or
        carry=0
        res=""
        a,b=a[::-1],b[::-1]

        for i in range(max(len(a),len(b))):
              dA=int(a[i]) if i < len(a) else 0
              dB=int(b[i]) if i < len(b) else 0
    
              total=dA+dB+carry
              char=str(total %2) 
              carry=total//2
              res=char+res
    
        if carry:
              res="1"+res
        return res
        
####################################################################




