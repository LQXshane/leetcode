
class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        if root in (None, target): return root
        
        tmp1_node = root.left if target < root.val else root.right
        
        if not tmp1_node: return root.val
        
        tmp2_val = self.closestValue(tmp1_node, target)
        
        return min((tmp2_val, root.val), key = lambda x: abs(target -x) )
            




class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        # can do this iteratively
        # by putting all valid node values in a list: path
        # and comparing target to each of them in(along) the path
        # clever!!
        
        path = []
        
        while root:
            path.append(root.val)
            root = root.left if target < root.val else root.right
            
        return min(path, key=lambda x: abs(x-target))
