import java.util.*;
// Definition for a binary tree node.
/*
class TreeNode {
      int val;
      TreeNode left;
      TreeNode right;
      TreeNode(int x) { val = x; }
    }
*/

class BTRightSideView {
  public List<Integer> rightSideView(TreeNode root) {
      List<Integer> result = new ArrayList();
      Queue<TreeNode> q = new LinkedList();
      if (root == null) return result;

      q.offer(root);
      while (q.size() != 0) {
          int n = q.size();
          for (int i = 0; i < n; i++) {
              TreeNode cur = q.poll();
              if (i == 0) result.add(cur.val);
              if (cur.right != null) q.offer(cur.right);
              if (cur.left != null) q.offer(cur.left);
          }
      }
      return result;
  }
}
