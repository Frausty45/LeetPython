from typing import Optional

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

root = TreeNode(3)
nodeA = TreeNode(9)
nodeB = TreeNode(20)
nodeC = TreeNode(15)
nodeD = TreeNode(7)

root.left = nodeA
root.right = nodeB
nodeB.left = nodeC
nodeB.right = nodeD

print("root.right.left.data: ", root.right.left.data)
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        else:
            return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

sol = Solution()
depth = sol.maxDepth(root)
print(depth)
