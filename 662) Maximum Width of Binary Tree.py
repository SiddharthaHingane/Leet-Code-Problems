# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Node:
    def __init__(self, node, ind):
        self.node = node
        self.ind = ind

class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if root is None:
            return 0
        ans = 0
        q = deque()
        q.append(Node(root, 0))
        start, end = 0, 0
        while q:
            offsetMin = q[0].ind
            size = len(q)
            for i in range(size):
                curInd = q[0].ind - offsetMin
                child = q[0].node
                q.popleft()
                if i == 0:
                    start = curInd
                if i == size - 1:
                    end = curInd
                if child.left is not None:
                    q.append(Node(child.left, 2 * curInd + 1))
                if child.right is not None:
                    q.append(Node(child.right, 2 * curInd + 2))
            ans = max(ans, end - start + 1)
        return ans
