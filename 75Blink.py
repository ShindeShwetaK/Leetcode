############https://leetcode.com/studyplan/leetcode-75/#################
############################Array String################################

#Q1 Merg string Alternately
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        new_string = ""
        max_len = max(len(word1), len(word2))

        for i in range(max_len):
            if i <len(word1):
                new_string += word1[i]

            if i < len(word2):
                new_string += word2[i]

        return new_string

#OR
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        new_string = []
        
        for i,j in zip(word1, word2):
            new_string.append(i)
            new_string.append(j)

        new_string.append(word1[len(word2):])
        new_string.append(word2[len(word1):])

        return "".join(new_string)

###################################################################
#Q2. Find Greatest Substring.

def gcdOfStrings(self, str1: str, str2: str) -> str:
    def gdc(a ,b):
        while b:
            a , b = b , a % b
        return a
    return str1([ :gcd(len(str1), len(str2) ]) if str 2 +str1 == str1 + str2 else ''

####################################################################
#Q3. Extra Candies

    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        candies_status = []
        max_candy = max(candies)

        for i in range(len(candies)):
           count = candies[i] + extraCandies
           if count >= max_candy:
              candies_status.append(True)
           else:
              candies_status.append(False)

        return candies_status

###################################################################
#Q4. FlowerBed Problem
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowerbed= [0]+flowerbed+[0]
        for i in range(1,len(flowerbed)-1):
            if flowerbed[i] == 0 and flowerbed[i-1] == 0  and flowerbed[i+1] == 0:
                flowerbed[i] = 1
                n =-1
        if n<=0:
            return True
        else:
            return False
#######################################################################
#Q5 Vowels interchange
 def reverseVowels(self, s: str) -> str:
        s = list(s)
        vowel = set('aeiouAEIOU')
        left , right = 0, len(s) - 1

        while left < right:
            if s[left] not in vowel:
                left += 1
            elif s[right] not in vowel:
                right -= 1
            else:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
            return "".join(s) 
####################################################################################################
#Q6 Reverse the Strings
     class Solution:
    def reverseWords(self, s: str) -> str:
        word = s.split()
        reverse = []

        for i in range(len(word)-1, -1, -1):
            reverse.append(word[i])      
            if i!=0:
                reverse.append(" ") 

        return "".join(reverse) 

#########################################################################################
#Q7 Product or arry without self
        class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        product = [1] * n

        prefix = 1
        for i in range(n):
            product[i] *= prefix
            prefix *= nums[i]

        suffix = 1
        for i in range(n-1, -1, -1):
            product[i] *= suffix
            suffix *= nums[i]

        return product
############################################################################################
#Q8. 
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = float('inf')
        second = float('inf')
        
        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True
        
        return False
###################################################################################



#####################################################
#Linked_list##########################################
#Q141  https://leetcode.com/problems/linked-list-cycle/description/#
 def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        while fast and fast.next:
            slow= slow.next
            fast = fast.next.next
            if fast == slow:
                return True


        return False
#######################################################################################
##Q143###################
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        prev = slow.next = None
        while second:
            next_node = second.next
            second.next = prev
            prev = second
            second = next_node

        first , second = head , prev
        while second:
           temp_list1 , temp_list2 = first.next, second.next
           first.next = second
           second.next = temp_list1
           first , second =  temp_list1 , temp_list2     

######################################################################################
####Q2095 Delete middle node####
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None: return None
        prev = ListNode(0)
        prev.next = head
        next_node = head
        slow = prev
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        slow.next = slow.next.next
        return prev.next

######################################################################################
###Q206 Reverse the LL
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None: return None

        prev = None
        current = head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        return prev
#############################################################################################
##Q 21 Merging 2 linkedlist
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy

        while list1 and list2:
            if list1.val > list2.val:
                cur.next = list2
                list2 = list2.next
            else:
                cur.next = list1
                list1 = list1.next
            
            cur = cur.next
        
        if list1:
            cur.next = list1
        else:
            cur.next = list2
        
        return dummy.next

############################################################################################
##Q2130 Max Sum for LL
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow , fast = head, head
        maxVal = 0

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        while slow:
            next_node = slow.next
            slow.next = prev
            prev = slow
            slow = next_node
        
        while prev:
            maxVal = max(maxVal, head.val + prev.val)
            head = head.next
            prev = prev.next

        return maxVal

####################################################################################
# Adding 2 LL with carry
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode()
        res = dummy

        total = carry = 0

        while l1 or l2 or carry:
            total = carry

            if l1:
                total += l1.val
                l1 = l1.next
            if l2:
                total += l2.val
                l2 = l2.next
            
            num = total % 10
            carry = total // 10
            dummy.next = ListNode(num)
            dummy = dummy.next
        
        return res.next
#########################################################################################
# Q19 Remove nth node from behind
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        res = ListNode(0,head)
        dummy = res

        for i in range(n):
            head = head.next

        while head:
            head = head.next
            dummy = dummy.next

        dummy.next = dummy.next.next

        return res.next
    #########################################################################
#Q203 Remove the given val from LL
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        main = ListNode(0, head)
        helper = main

        while helper:
            while helper.next and helper.next.val == val:
                helper.next = helper.next.next
            helper = helper.next

        return main.next

###############################################################
#Q234 Palindrom
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        list_vals = []
        while head:
            list_vals.append(head.val)
            head = head.next

        l, r =0, len(list_vals)-1

        while l < r and list_vals[l] == list_vals[r]:
            l += 1
            r -= 1

        return l >= r
###########################################################
#############Hash Map######################
#Q 49 Anagram problem
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = defaultdict(list)
        return_result = []

        for s in strs:
            sort_s = tuple(sorted(s))
            anagram[sort_s].append(s)

        for i in anagram.values():
            return_result.append(i)

        return return_result

###########################################################
#Q2215. Find diff of two array
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        num1 = set(nums1)
        num2 = set(nums2)

        unique_nums1 = num1 - num2
        unique_nums2 = num2 - num1

        return [list(unique_nums1),list(unique_nums2)]

##########################################################
#Q1207. Unique number of occurence
from collections import Counter
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count_num = Counter(arr)

        duplicate = set()
        for i in count_num.values():
            if i in duplicate:
                return False
            else:
                duplicate.add(i)
        
        return True

#######################################################
#Q1657.Determine if 2 strings are close
from collections import Counter
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        n1=len(word1)
        n2=len(word2)
        if n1!=n2:
            return False
        cnt1=Counter(word1)
        cnt2=Counter(word2)
        lst1=list(cnt1.values())
        lst2=list(cnt2.values())
        for i in range(26):
            if (cnt1[chr(ord('a')+i)]==0 and cnt2[chr(ord('a')+i)]!=0) or (cnt2[chr(ord('a')+i)]==0 and cnt1[chr(ord('a')+i)]!=0):
                return False
        lst1.sort()
        lst2.sort()
        return lst1[:]==lst2[:]
        

##############################################
# Q # divided string
class Solution:
    def stringHash(self, s: str, k: int) -> str:
        result = ""
        n = len(s)

        for i in range(0, n, k):
            substring = s[i:i+k]

            hash_sum = sum(ord(char) - ord('a') for char in substring)

            hashed_char = hash_sum % 26

            result += chr(hashed_char + ord('a'))
        
        return result

##########################################################
#Q621 Schedule Task
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Count the frequency of each task
        frequencies = Counter(tasks)

        # Sort the frequencies in descending order
        frequencies = sorted(frequencies.values(), reverse=True)

        # The maximum frequency
        max_freq = frequencies[0]

        # Calculate the maximum possible idle time
        idle_time = (max_freq - 1) * n

        # Reduce idle time based on the remaining tasks
        for freq in frequencies[1:]:
            idle_time -= min(max_freq - 1, freq)

        # Idle time can't be negative
        idle_time = max(0, idle_time)

        # Total time is the sum of tasks and the remaining idle time
        return len(tasks) + idle_time
##########################################################################################
########Stack###########
#Q20 Valid Parentheses
class Solution:
    def isValid(self, s: str) -> bool:
        brackets_coll = {
            ")" : "(",
            "}" : "{",
            "]" : "["        }
        stack =[]

        for i in s:
            if i in brackets_coll:
                if not stack:
                    return False
                top = stack.pop()
                if brackets_coll[i] != top:
                    return False
            else:
                stack.append(i)

        if stack :
            return False
        else:
            return True

###################################################################
# Q2390. Removing Stars From a String.
#Using String Can give error of time limit exceeded
class Solution:
    def removeStars(self, s: str) -> str:
        res = ""
        i = 0
        while i < len(s):
            if s[i] == '*':  
                res = res[:-1]  # Remove the last character from res
                print(res,res[:-1])
                i += 1 
            else:
                res += s[i]
                i += 1
        return res

#Using Stack
    def removeStars(self, s: str) -> str:
        #Make a list in which you will add or remove the element
        word=[]
        #Iterate through the s until the end
        for i in s:
        #if * come while iteration pop the elements else append it to the list
            if i=="*":
                word.pop()
            else:
                word.append(i)
        #Convert the list into string and then return it
        return "".join(word)

########################################################################
#735 Asteroid Collision
        res = []

        for a in asteroids:

            while res and a < 0 < res[-1]:
                if -a > res[-1]:
                    res.pop()
                    continue
                elif -a == res[-1]:
                    res.pop()
                break
            else:
                res.append(a)

        return res
        ##################################################################################
###@394 Decode string 
        stack = []
        
        for c in s:
            if c != ']':
                stack.append(c)
            else:
                # Step 1: Pop until we hit the '[' to get the encoded substring
                st = ''
                while stack and stack[-1] != '[':
                    st = stack.pop() + st
                
                # Step 2: Pop the '['
                stack.pop()
                
                # Step 3: Pop the number k (repeat count)
                num = ''
                while stack and stack[-1].isnumeric():
                    num = stack.pop() + num
                
                # Step 4: Repeat the string 'st' k times and push it back to stack
                stack.append(int(num)*st)
        
        # Step 5: Join everything in the stack and return the result
        return ''.join(stack)
##############################################################################
#Q.71 Simplify Path
class Solution:
    def simplifyPath(self, path: str) -> str:
        dirFiles = []
        path = path.split("/")
        for i in path:
            if dirFiles and i == ".." :
                dirFiles.pop()
            elif i not in [".","",".."]:
                dirFiles.append(i)

        return "/" + "/".join(dirFiles)


If path = "/home//foo/" and you apply path.split("/"), the output will be: ['', 'home', '', 'foo', '']
###############################################################################
#Q Baseball Game.
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        for i in operations:
            if i.isdigit() or (i.startswith('-') and i[1:].isdigit()):
                record.append(int(i))
            elif i == "C":
                if record:
                    record.pop()
            elif i == "D":
                if record:
                    record.append(record[-1]*2)
            elif i == "+":
                if len(record) >= 2:
                    record.append(record[-1] + record[-2])        
        return sum(record)

#############################################################################
##Sliding Window##########################
#Q643. Max_avg Substring
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        avg_sum = sum(nums[:k])
        max_avg = avg_sum / k
        for i in range(k, len(nums)):
            avg_sum = avg_sum + nums[i] - nums[i-k]
            max_avg = max(max_avg, avg_sum/k)

        return max_avg
########################################################
#Q1456 Max number of Vowels in substr
        vowel = 0 
        for i in range(k):
            if s[i] in "aeiou":
                vowel += 1
        max_v = vowel

        for i in range(k,len(s)):
            if s[i] in "aeiou":
                vowel += 1
            if s[i-k] in "aeiou":
                vowel -= 1
            max_v = max(max_v, vowel)

        return max_v

#################################################
#Q1004 Max consecutive 1
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l =  0

        for r in range(len(nums)):
            if nums[r] == 0:
                k -= 1

            if k<0:
                if nums[l] == 0:
                    k += 1

                l +=1

        return r - l+1
############################################
#Q 219 Cointains duplicate at K
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = {}

        for i, val in enumerate(nums):
            if val in seen and i -seen[val] <= k:
                return True
            else:
                seen[val] = i

        return False
#############################################
#Q340 Longest substring 
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        win_len = 0
        start = 0

        for i in range(len(s)):
            if (len(set(s[start:i+1]))) <= k:
                win_len = max(win_len , len(s[start:i+1]))
            else :
                start +=1

        return win_len
###################################################################
#Q187 Repeating DNA
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        set1 = set()
        set2 = set()

        p0 = 0
        p1 = 10
        while p1 <= len(s):

            if s[p0:p1] in set1:
                set2.add(s[p0:p1])
            else:
                set1.add(s[p0:p1])
            
            p0+=1
            p1+=1

        return list(set2)

##################################################################
#Q1732 Prefix Problem
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitude = [0]

        for i in range(len(gain)):
            altitude.append(altitude[i] + gain[i])

        return max(altitude)
#################################################################
#Q724 Pivorting Index
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        left_total = 0

        for i in range(len(nums)):
            right_total = total - left_total-nums[i]

            if right_total == left_total:
                return i
            
            left_total += nums[i]

        return -1

###################################################################
#Q Implementing queue with stack
class MyQueue:

    def __init__(self):
        self.q=deque()
        

    def push(self, x: int) -> None:
        self.q.append(x)
        

    def pop(self) -> int:
        return self.q.popleft()
        

    def peek(self) -> int:
        return self.q[0]
        

    def empty(self) -> bool:
        return len(self.q) == 0
######################################################################
#Q281 ZigZag Iterator
class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.d = deque()
        if v1:
            self.d.append((0,v1))
        if v2:
            self.d.append((0,v2))
 
        

    def next(self) -> int:
        i, v = self.d.popleft()
        res = v[i]
        i += 1
        if i < len(v):
            self.d.append((i, v))
        return res
#################################################################################
#933. Number of Recent Calls
class RecentCounter:

    def __init__(self):
        self.queue = deque()
        self.count = 0
        

    def ping(self, t: int) -> int:
        self.queue.append(t)
        self.count += 1

        while self.queue[0] < t-3000:
            self.queue.popleft()
            self.count -= 1

        return self.count
##############################################
#1352. Product of the Last K Numbers
class ProductOfNumbers:

    def __init__(self):
        self.product = [1]

        

    def add(self, num: int) -> None:
        if num == 0:
            self.product = [1]
        else:
            self.product.append(self.product[-1] * num)
        

    def getProduct(self, k: int) -> int:
        if k >= len(self.product):
            return 0
        else:
            return self.product[-1] // self.product[-1-k]

##################################################################
#Q450. Deletenodes in BST
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def findmin(self, root):
        current = root
        while current.left:
            current = current.left
        return current
    
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return root
        
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        
        else:
            #leaf
            if not root.left and not root.right:
                root = None
            
            # 1 child
            elif not root.left:
                root = root.right
            
            elif not root.right:
                root = root.left
            
            else:
                temp = self.findmin(root.right)
                root.val = temp.val
                root.right = self.deleteNode(root.right, temp.val)
        return root













        
        
    

