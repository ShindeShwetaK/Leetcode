408. Valid Word Abbreviation
class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i = 0  # pointer for abbr
        j = 0  # pointer for word

        while i < len(abbr):
            # check for leading zero
            if abbr[i] == '0':
                return False

            number = ""
            # collect digits into full number
            while i < len(abbr) and abbr[i].isdigit():
                number += abbr[i]
                i += 1

            if number:  # skip those many characters
                j += int(number)
                if j > len(word):
                    return False
            else:  # handle letter
                if j >= len(word) or abbr[i] != word[j]:
                    return False
                j += 1
                i += 1  # move forward only after letter match

        return j == len(word)

      ---------------------------------------------------------
      680. Valid Palindrome II
      l = 0
      r=0

      while l<r:
        if s[l] == s[r]:
            l+=1
            r-=1
        else:
           return s[l:r] == s[l:r][::1] or s[l+1:r+1] == s[l+1:r+1][::1]
      return True
      ----------------------------------------------------------
199. Binary Tree Right Side View
res = []

q = deque()
q.append(root)

while q:
    right_side = None
    for _ in range(len(q)):
        node = leftpop()
        if node:
            right_side = node
            q.append(node.left)
            q.appen(node.right)
    if right_side:
        res.append(right_side)
return res
----------------------------------------
215. Kth Largest Element in an Array
q = nums[:k]
heap.heapify(q)

for i in range(k,len(nums)):
    if num[i] > q[0]:
        heapq.heappush(q,nums[i])
        healq.heappop(q)
return heap.heappop(q)

-------------------------------------
71. Simplify Path
dirfiles = []
path = path.split("/")

for i in path:
    if dirfile and i == "..":
        dirfile.pop()
    if i not in [".","..",""]:
        dirfiles.append(i)

return "/" + "/".join(dirfiles)
-------------------------------------
1 2 sum

for i in range(0, len(num)):
    for j in range(i+1,len(nums)):
        if nums[i] +num[j] = target:
            return [i,j]

d ={}
for i , n in enumerate(nums):
    diff = target - n 
    if diff in d:
        return [d[diff, i]
    d[n] = i

-------------------------------
1249.Minimum Remove to Make Valid Parentheses

open = 0
bal = 0

char_list = []
for char in s:
    if char == "(":
        open += 1
        bal += 1
    if char == ")":
        if bal == 0:
            continue
        bal -= 1
    char_list.append(char)

total_open = open - bal

result = []

for char in char_list:
    if char == "(":
        total_open -= 1
        if total_open < 0:
            continue
    result.append(char)

returb result
-----------------------------------
347. Top K Frequent Elements
counter = {}
for i in nums:
    if i in counter:
        counter[i] += 1
    else:
        counter[i] = 1

heap = []
for key, val in counter.iteam():
    heapq.heappush(heap,(-val,key))

res = []
while len(res) < k:
    res.append(heapq.heappop(heap)[1])
return res

-----------------------------------
def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
    self.ans = 0
    def dfs(self.node) -> int:
        if not node:
            return -1
        lh = dfs(node.left) + 1
        rh = dfs(node.right) + 1
        self.ans = max(self.ans, lh+rh)
        return max(lh,rh)

    dfs(root)
    return self.ans
----------------------------------
Subarray sum equals
count = 0
for i in range(len(nums)):
    total = 0 
    for j in range(i,len(nums)):
        total += nums[j]
        if total == k:
            count += 1
return count
or
count = 0
prefix = 0
feq = {O:1}

for i in nums:
    prefix += i
    if prefix - k in feq:
        count += feq[prefix - k]
    if prefix in feq:
        feq[prefix] += 1
    else:
        feq[prefix] = 1
return count
        
