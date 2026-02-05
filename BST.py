
################################################
#Q700. Search in a Binary Search Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return None
        if root.val == val:
            return root

        if root.val > val:
            return self.searchBST(root.left,val)
        else:
            return self.searchBST(root.right,val)
#######################################################################
#104. Maximum Depth of Binary Tree
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        return 1+ max(self.maxDepth(root.left), self.maxDepth(root.right))
    #################################################################
#q
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        leftLeafNodeList = [] 
        self.leafNode(root1,leftLeafNodeList)
        rightLeafNodeList = [] 
        self.leafNode(root2,rightLeafNodeList)

        if leftLeafNodeList == rightLeafNodeList:
            return True
        else:
            return False
    


    def leafNode(self, root: Optional[TreeNode],leafNodeList:Optional[list])-> None :
            # leafNodelist =[]
            if root  is None:
                return 
            
            if root.left is None and root.right is None:
                leafNodeList.append(root.val)
                return 
            
            self.leafNode(root.left,leafNodeList)
            self.leafNode(root.right,leafNodeList)

###########################################
102. Binary Tree Level Order Traversal
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        if not root:
            return res

        q = collections.deque()
        q.append(root)

        while q:
            same_level = []       

            for _ in range(len(q)):
                node = q.popleft()
                same_level.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            res.append(same_level)

        return res

###########################################
107.Binary Tree Level Order Traversal II
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not root:
            return []

        q = collections.deque()
        q.append(root)

        while q:
            arr = []
            for _ in range(len(q)):
                node = q.popleft()
                arr.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            res.append(arr)

        return res[::-1]

######################################
993. Cousins in Binary Tree
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        if not root:
            return False

        res = []

        q = deque([(root, None, 0)])

        while q:
            if len(res) == 2:
                break 

            node, parent, depth = q.popleft()

            if node.val == x or node.val == y:
                res.append((parent, depth))

            if node.left:
                q.append((node.left, node, depth + 1))

            if node.right:
                q.append((node.right, node, depth + 1))

        node_x, node_y = res

        return node_x[0] != node_y[0] and node_x[1] == node_y[1]

##################################################
994. rotten oranges

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = grid
        q = collections.deque()
        countFreshOrange = 0
        for i in range(m):
            for j in range(n):
                if visited[i][j] == 2:
                    q.append((i, j))
                if visited[i][j] == 1:
                    countFreshOrange += 1
        if countFreshOrange == 0:
            return 0
        if not q:
            return -1
        
        minutes = -1
        dirs = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        while q:
            size = len(q)
            while size > 0:
                x, y = q.popleft()
                size -= 1
                for dx, dy in dirs:
                    i, j = x + dx, y + dy
                    if 0 <= i < m and 0 <= j < n and visited[i][j] == 1:
                        visited[i][j] = 2
                        countFreshOrange -= 1
                        q.append((i, j))
            minutes += 1
        
        if countFreshOrange == 0:
            return minutes
        return -1
