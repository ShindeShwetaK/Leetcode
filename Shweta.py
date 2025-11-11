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
