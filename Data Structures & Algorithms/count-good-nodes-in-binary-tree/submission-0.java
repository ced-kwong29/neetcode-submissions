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
    private int count = 0;

    private void count(TreeNode root, List<Integer> seen) {
        if (root == null) {
            return;
        }

        boolean good = true;
        for (int v : seen) {
            if (v > root.val) {
                good = false;
                break;
            }
        }
        if (good) {
            count++;
        }

        seen.add(root.val);
        count(root.left, seen);
        count(root.right, seen);
        seen.remove(seen.size() - 1);
    }

    public int goodNodes(TreeNode root) {
        count(root, new ArrayList<>());
        return count;
    }
}
