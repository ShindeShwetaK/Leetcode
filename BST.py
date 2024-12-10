
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

