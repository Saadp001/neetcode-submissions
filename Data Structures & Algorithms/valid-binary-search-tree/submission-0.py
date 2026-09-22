# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def solve(node):
            if not node:
                return float('-inf'), float('inf'), True

            lmax, lmin, lflag = solve(node.left)
            rmax, rmin, rflag = solve(node.right)
 
            maxi = max(lmax, rmax, node.val)
            mini = min(lmin, rmin, node.val)

            flag = (
                lflag and rflag and
                lmax < node.val and 
                node.val < rmin
            )   

            return maxi, mini, flag

        maxi, mini, flag = solve(root)
        return flag
