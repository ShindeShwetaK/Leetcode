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
