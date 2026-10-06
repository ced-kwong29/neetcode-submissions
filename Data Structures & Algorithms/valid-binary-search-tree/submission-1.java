/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    private boolean validate(TreeNode root, long minVal, long maxVal) {
        if (root == null) {
            return true;
        }

        long val = (long) root.val;
        if (val <= minVal || val >= maxVal) {
            return false;
        }
        return validate(root.left, minVal, val) && validate(root.right, val, maxVal);
    }

    public boolean isValidBST(TreeNode root) {
        return validate(root, Long.MIN_VALUE, Long.MAX_VALUE);
    }
}
