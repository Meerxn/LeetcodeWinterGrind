# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        return self.printLevelOrder(root)
        
    
# Python program to print level
# order traversal using Queue
 
# A node structure
 

 
    def printLevelOrder(self,root):
        res = []
        if root is None:
            return

  
        queue = []

        queue.append(root)
        

        while(len(queue) > 0):
            temp = []
            for i in range(len(queue)):
    
                
                node = queue.pop(0)
                if node:
                    temp.append(node.val)
                    # Enqueue left child
                    if node.left is not None:
                        queue.append(node.left)


                    # Enqueue right child
                    if node.right is not None:
                        queue.append(node.right)
            res.append(temp)
        return res 
                
                    
                
            
          