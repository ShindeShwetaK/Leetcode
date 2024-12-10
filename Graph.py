##############################################
##841. Keys and Rooms
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        def dfs(room):
            visited.add(room)
            for key in rooms[room]:
                if key not in visited:
                    dfs(key)

        visited = set()
        dfs(0)
        return len(rooms) == len(visited)

rooms =
[[1,3],[3,0,1],[2],[0]]

0 [1, 3]
key 1
1 [3, 0, 1]
key 3
3 [0]

#Here we cannot visit 2 so false

#############################################################
#Q100 Same tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True

        if p and q and p.val == q.val:
            return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)

        return False

#####################################################
#Q101. Symmetric Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def mirror(n1,n2):
            if not n1 and not n2:
                return True

            if not n1 or not n2:
                return False

            if n1.val == n2.val:
                return mirror(n1.left, n2.right) and mirror(n1.right, n2.left)

            return False
            
        return mirror(root.left , root.right)

######################################################
#102. Binary Tree Level Order Traversal
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = collections.deque()
        q.append(root)
        while q:
            q_len = len(q)
            level = []
            for i in range(q_len):
                node = q.popleft()
                if node is not None:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                res.append(level)
        return res

############################################################
#111. Minimum Depth of Binary Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        if not root.left:
            return self.minDepth(root.right)+1

        if not root.right:
            return self.minDepth(root.left)+1

        if not root.left and root.right:
            return 1

        return 1+ min(self.minDepth(root.left), self.minDepth(root.right))

##################################################################
#Q Sum of left leaves
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        leftsum = 0

        if root.left and not root.left.left and not root.left.right:
            leftsum += root.left.val

        leftsum += self.sumOfLeftLeaves(root.left)
        leftsum += self.sumOfLeftLeaves(root.right)

        return leftsum
        ##########################################################
#Iland problem
def islandPerimeter(grid):
    rows, cols = len(grid), len(grid[0])
    perimeter = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:  # Land cell
                # Start with 4 edges for this cell
                perimeter += 4

                # Check for neighbors and subtract shared edges
                if i > 0 and grid[i-1][j] == 1:  # Up neighbor
                    perimeter -= 1
                if i < rows - 1 and grid[i+1][j] == 1:  # Down neighbor
                    perimeter -= 1
                if j > 0 and grid[i][j-1] == 1:  # Left neighbor
                    perimeter -= 1
                if j < cols - 1 and grid[i][j+1] == 1:  # Right neighbor
                    perimeter -= 1

    return perimeter

######################################################################
#Merge 2 Binarytrees
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:

        def dfs(node1, node2):
            if node1 and node2:
               root = TreeNode(node1.val + node2.val)
               root.left = dfs(node1.left, node2.left)
               root.right = dfs(node1.right, node2.right)
               return root

            else:
                return node1 or node2
        
        return dfs(root1, root2)
        
