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


        



