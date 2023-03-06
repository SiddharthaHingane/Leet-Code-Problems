class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        if not root: return res
        stack = [[root, [root.val]]]
        while len(stack) > 0:
            node, path = stack.pop()
            if not node.left and not node.right and sum(path) == targetSum:
                res.append(path)
            if node.right:
                stack.append([node.right, path + [node.right.val]])
            if node.left:
                stack.append([node.left, path + [node.left.val]])
        return res
