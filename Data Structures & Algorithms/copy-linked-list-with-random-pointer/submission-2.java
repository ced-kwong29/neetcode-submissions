/*
// Definition for a Node.
class Node {
    int val;
    Node next;
    Node random;

    public Node(int val) {
        this.val = val;
        this.next = null;
        this.random = null;
    }
}
*/

class Solution {
    public Node copyRandomList(Node head) {
        if (head == null) {
            return null;
        }
        Map<Node, Node> nodeMapping = new HashMap<>();
        nodeMapping.put(head, new Node(head.val));

        Node pos = head;
        while (pos != null) {
            if (pos.next != null) {
                if (!nodeMapping.containsKey(pos.next)) {
                    nodeMapping.put(pos.next, new Node(pos.next.val));
                }
                nodeMapping.get(pos).next = nodeMapping.get(pos.next);
            }
            if (pos.random != null) {
                if (!nodeMapping.containsKey(pos.random)) {
                    nodeMapping.put(pos.random, new Node(pos.random.val));
                }
                nodeMapping.get(pos).random = nodeMapping.get(pos.random);
            }

            pos = pos.next;
        }

        return nodeMapping.get(head);
    }
}
