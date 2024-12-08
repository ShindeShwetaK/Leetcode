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










        
        
    

