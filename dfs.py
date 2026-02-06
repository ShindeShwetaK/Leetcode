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
