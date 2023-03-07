# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths(self, root: TreeNode) -> int:
        count = 0
        # root = [2,3,1,3,1,null,1]

        stack = [(root, 0)]
        # path = 00000000
        # nade = 2
        # 1 << node.val = 1 << 2 = 00000100
        # path = 00000100
        # node = 3
        # 1 << node.val = 00001000
        # path = 00001100
        # node =3
        # 1 << node.val = 00001000
        # path = 00000100
        # path & (path -1)
        # path -1 = 00000011
        # count =1

        while stack:
            node, path = stack.pop()
            if node is not None:
                path = path ^ (1 << node.val)
                # if it's a leaf, check if the path is pseudo-palindromic
                if node.left is None and node.right is None:
                    # check if at most one digit has an odd frequency
                    if path & (path - 1) == 0:
                        count += 1
                else:
                    stack.append((node.left, path))
                    stack.append((node.right, path))

        return count
