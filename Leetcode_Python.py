#My Solution
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
#####################################################################
#Q11. Container Porblem
class Solution:
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
	##Linear solution o(logn)

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
#Q33. Search in rotated sorted array
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r=0,len(nums)-1

        while l<=r:
            mid=(l+r)//2
            if target == nums[mid]:
                return mid

   
             #left portion
            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]:
                    l=mid+1
                else:
                    r=mid-1
             #right postion
            else:
                if target < nums[mid] or target > nums[r]:
                    r=mid-1
                else:
                    l=mid+1
        return -1
	    #o(log n) as no for loop is used
#####################################################################
#Q49.Group Anagrams
#https://leetcode.com/problems/group-anagrams/
    from collections import defaultdict
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_list=defaultdict(list)
        result=[]
        for s in strs:
            sorted_s=tuple(sorted(s))
            anagrams_list[sorted_s].append(s)
        for i in anagrams_list.values():
            result.append(i)
        return result

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
#Q53. Maximax Subarray
    def maxSubArray(self, nums: List[int]) -> int:
        maxsub= nums[0]
        cursum=0

        for i in nums:
            if cursum < 0:
                cursum=0
            cursum+=i
            maxsub= max(maxsub,cursum)
        return maxsub
#O(n)
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
#Q152.Maximum Product Subarray

   class Solution:
         def maxProduct(self, nums: List[int]) -> int:
            res=max(nums)
            curmin,curmax=1,1

            for n in nums:
                 tmp=n*curmax
                 curmax=max(n*curmax,n*curmin,n)
                 curmin=min(tmp,n*curmin,n)
                 res=max(res,curmax)
            return res
	 #o(n)
###################################################################
#Q153.Find Minimum in Rotated Sorted Array
        res=nums[0]
        l,r=0,len(nums)-1

        while l<=r:
            if nums[l]<nums[r]:
                res=min(res,nums[l])
                break
            
            m=(l+r)//2
            res=min(res,nums[m])
            if nums[m]>=nums[l]:
                l=m+1
            else:
                r=m-1
        return res
  #o(lon n) as we have not used any for loop
##################################################################

        
####################################################################
#Q121. Best Time to Buy and Sell Stock
  def maxProfit(self, prices: List[int]) -> int:
        l=0
        r=1
        max_p=0

        while r < len(prices):
            if prices[l] < prices[r]:
               profit=prices[r]-prices[l]
               max_p=max(max_p,profit)
            else:
                l=r
            r+=1
        return max_p
####################################################################
#Q.191. number of 1 bit
class Solution:
    def hammingWeight(self, n: int) -> int:
        res=0
        while n:
            res += n%2   # Add 1 if the least significant bit is 1, otherwise add 0
            n= n>>1      # Shift right by 1 bit (divide by 2)
        return res
        
####################################################################
#Q217. Duplicates in Array.
    hashset=set()
    for n in nums:
	    if n in hashset:
		    return True
	    else:
		    hashset.add(n)
    return False
######################################################################
#Q238.Product of an array except self
#below solution will give exceed time limit error because we have 2 loops so O(n^2)
          pre=1
          output=[]
          for i in range(len(nums)):
               pre=1
               for j in range(0,len(nums)):
                    if j != i:
                        pre *=nums[j]
               output.insert(i,pre)
          return output
#best solution as we have 1 loop so O(n)
        output=[1] * len(nums)

         pre=1
         for i in range(len(nums)):
             output[i]=pre
             pre*=nums[i]

         post=1
         for i in range(len(nums)-1,-1,-1):
             output[i]*=post
             post*=nums[i]
################################################################
res=cur=0
for i,j in zip([-float('inf')]+price,price):    
    cur=1+cur*(j>i)    
    res+=cur>=k        
return res
         
         return output
############################################################
#Goldman shak
#https://leetcode.com/discuss/interview-question/5519855/Goldman-Sachs-or-Online-Assessment-or-Crack-the-Lock
def can_reach_target(N, P, X, M):
    """
    Determine if the gold key can be moved to position X starting from position P
    by reversing M consecutive keys that include the gold key.
    """
    if P == X:
        return True

    # Breadth-First Search (BFS) to explore all possible positions
    from collections import deque
    
    queue = deque([P])
    visited = set([P])
    
    while queue:
        current = queue.popleft()
        
        # Check all possible segments including the gold key
        start_min = max(1, current - M + 1)
        start_max = min(N - M + 1, current)
        
        for start in range(start_min, start_max + 1):
            new_position = 2 * start + M - 1 - current
            if 1 <= new_position <= N and new_position not in visited:
                if new_position == X:
                    return True
                visited.add(new_position)
                queue.append(new_position)
    
    return False

def determine_winner(N, P, X, M):
    """
    Determine the winner of the game or if it's a draw.
    """
    # Steve starts first, so we only need to check if the target position is reachable
    if can_reach_target(N, P, X, M):
        return "Steve"
    else:
        return "Harvey"

# Example usage
N = 5
P = 2
X = 5
M = 3

print(determine_winner(N, P, X, M))
#########################################################################
#Q724. Find first pivot index
          total=sum(nums)
          leftsum=0
          for i in range(len(nums)):
            rightsum=total-nums[i]-leftsum
            if leftsum==rightsum:
                return i
            leftsum+=nums[i]
          return -1
#############################################################################
#Q1356. Sort Integers by The Number of 1 Bits
        arr.sort()
        d={}
        for i in arr:
           count=bin(i).count('1')
           if count not in d:
             d[count]=[i]
           else:
             d[count].append(i)
        res=[]
        for i in sorted(d.keys()):
           res.extend(d[i])
        return res
############################################################################
#Q189 Rotate array inplace
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        while k!=0:
            nums.insert(0,nums[-1])
            nums.pop(-1)
            k-=1
###########################################################################
#Q136 Find unique in array
    def singleNumber(self, nums: List[int]) -> int:
        for i in nums:
            if nums.count(i)==1:
                return i


