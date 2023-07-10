# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        queue = deque()
        queue.append(root)
        depth = 0
        
        while queue:
            size = len(queue)
            depth += 1
            
            for _ in range(size):
                node = queue.popleft()
                
                if not node.left and not node.right:
                    return depth
                
                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)
        
        return 0  # In case the tree is empty
