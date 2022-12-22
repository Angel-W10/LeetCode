# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
class Solution:
    def insertIntoBST(self, root, val):
        if(root == None):
            root = TreeNode(val)
        else:
            temp = root
            if(val < temp.val):
                if(temp.left == None):
                    temp.left = TreeNode(val)
                else:
                    self.insertIntoBST(temp.left, val)
            if(val > temp.val):
                if(temp.right == None):
                    temp.right = TreeNode(val)
                else:
                    self.insertIntoBST(temp.right, val)

        return root

    
