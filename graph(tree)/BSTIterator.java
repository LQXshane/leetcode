tion for binary tree
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */

public class BSTIterator {
    
    private Stack<TreeNode> s = new Stack<TreeNode>();

    public BSTIterator(TreeNode root) {
        
        pushAll(root);
        
    }

    /** @return whether we have a next smallest number */
    public boolean hasNext() {
        
        return !s.isEmpty();
        
    }

    /** @return the next smallest number */
    public int next() {
        
        TreeNode tmp = s.pop();
        pushAll(tmp.right);
        return tmp.val;
        
    }
    
    private void pushAll(TreeNode node) {
        
        for (; node!= null; s.push(node), node = node.left);
        // nice way of abbreviate 'for' conditions
        
    }
}


/**
 * Your BSTIterator will be called like this:
 * BSTIterator i = new BSTIterator(root);
 * while (i.hasNext()) v[f()] = i.next();
 */
