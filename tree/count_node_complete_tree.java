# concise idea from https://discuss.leetcode.com/topic/15533/concise-java-solutions-o-log-n-2
# author: Stefan Pochmann
class Solution {
    int height(TreeNode root) {
        return root == null ? -1 : 1 + height(root.left);
    }// same idea: count sub tree heights
    public int countNodes(TreeNode root) {
        int h = height(root);
        return h < 0 ? 0 :
               height(root.right) == h-1 ? (1 << h) + countNodes(root.right)
                                         : (1 << h-1) + countNodes(root.left);
    }// he is using binary operators 1<<h same as 2 to the power of h

}
