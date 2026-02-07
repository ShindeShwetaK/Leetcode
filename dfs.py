617. Merge Two Binary Trees
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1:
            return root2

        elif not root2:
            return root1

        else:
            res = TreeNode(root1.val + root2.val)
            res.left = self.mergeTrees(root1.left, root2.left)
            res.right = self.mergeTrees(root1.right,root2.right)

        return res
#####################################################################
572. Subtree of Another Tree
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def same(a, b):
            if not a and not b:
                return True

            if a and b and a.val == b.val:
                return same(a.left, b.left) and same(a.right, b.right)

            return False

        if not root:
            return False

        if same(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

  #########################
200. Number of island
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid) , len(grid[0])
        island = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    island += 1
                    self.dfs(grid,r, c)

        return island

    def dfs(self, grid, r,c):

        if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] == "1" and (r, c):
            grid[r][c] = '#'
            self.dfs(grid, r - 1, c)
            self.dfs(grid, r + 1, c)
            self.dfs(grid, r, c - 1)
            self.dfs(grid, r, c + 1)
        else:
            return
############################################
695. Max Area of Island
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        max_island = 0

        def dfs(r, c):

            if 0 <= r < len(grid) and 0<= c < len(grid[0]) and grid[r][c] == 1:

                 grid[r][c] = 0
                 return 1 + (dfs(r - 1, c) + dfs(r + 1, c) + dfs(r, c - 1) + dfs(r, c + 1))

            else:
                return 0


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    max_island = max(max_island, dfs(r, c))

        return max_island

##########################################
547. Number of Provinces
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        province = 0
        visited = set()

        def dfs(city):
            visited.add(city)
            for curr, connected in enumerate(isConnected[city]):
                if connected and curr not in visited:
                    dfs(curr)
                    

        for i in range(len(isConnected)):
            if i not in visited:
                province += 1
                dfs(i)

        return province

##########################################
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or p == root or q == root:
            return root

        left = self.lowestCommonAncestor(root.left, p , q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if right and left:
            return root

        return right or left
###############################
199. Binary Tree Right Side View
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q = deque()
        q.append(root)

        while q:
            right_node = None
            for _ in range(len(q)):
                node = q.popleft()
                if node:
                    right_node = node
                    q.append(node.left)
                    q.append(node.right)
            if right_node:
                res.append(right_node.val)

        return res

#################################
144. Binary Tree Preorder Traversal

(iteration)
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        stack = [root]

        while stack:
            node= stack.pop()
            res.append(node.val)
            # Push right first so left is processed first
            if node.right:
                stack.append(node.right)

            if node.left:
                stack.append(node.left)

        return res

Inorder Stack
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        res = []
        stack = []

        while stack or root:
            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()
            res.append(root.val)

            root = root.right

        return res

o(n) and o(h)
space is height of the tree.
we visit every node once so o(n) time

post order
def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return []

        res = []
        stack = [root]

        while stack:
            node = stack.pop()
            res.append(node.val)

            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        return res[::-1]

recursion
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

result = []

def inorder(root):
    if not root:
        return []

    inorder(root.left)
    result.append(root.val)
    inorder(root.right)
    return result

def preorder(root):
    if not root:
        return []

    result.append(root.val)
    preorder(root.left)
    preorder(root.right)
    return result

def postorder(root):
    if not root:
        return []

    postorder(root.left)
    postorder(root.right)
    result.append(root.val)
    return result

################################
104. 104. Maximum Depth of Binary Tree
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        while root:
            return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

###############################
226. Invert Binary Tree

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return 

        stack = [root]

        while stack:
            node = stack.pop()

            node.left, node.right = node.right , node.left

            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        return root

BFS
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return 

        q = deque([root])

        while q:
            node = q.popleft()

            node.left, node.right = node.right , node.left

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return 

        temp = root.left
        root.left =  self.invertTree(root.right)
        root.right = self.invertTree(temp)

        return root

#####################################
841. Keys and Rooms
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

    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        keys = {key for key in rooms[0]}
        visited = set()
        visited.add(0)

        while keys:
            print(keys)
            val = keys.pop()
            print(val)
            if val not in visited:
                for i in rooms[val]:
                    keys.add(i)
                visited.add(val)

        return len(rooms) == len(visited) 



###############################
733.Flood fill
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        rows, cols = len(image), len(image[0])
        start = image[sr][sc]

        if start == color:
            return image

        q = deque([(sr,sc)])
        image[sr][sc] = color

        while q:
            r , c = q.popleft()
            dirs = [(1,0),(-1,0),(0,1),(0,-1)]

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                
                if 0<= nr < rows and 0 <= nc < cols and image[nr][nc] == start:
                    image[nr][nc] = color
                    q.append((nr, nc))

        return image

##################################


        



