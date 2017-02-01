
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class LCA{
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        
        if (root == null || root == p || root == q) return root;
        // evalute root==p only if the first condition(root==null) is false
        // for && operator: stop evaluate if the current condition is false
        // for &: evaluate all conditions then use the operator
        TreeNode left = lowestCommonAncestor(root.left, p, q);
        TreeNode right = lowestCommonAncestor(root.right, p, q);
        
        // condition operator
        return left == null ? right : right == null ? left : root;
    }
}

//http://www.geeksforgeeks.org/lowest-common-ancestor-binary-tree-set-1/
