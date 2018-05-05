import java.util.Scanner;

class Node
{
    Node left;
    Node right;
    int data;

    Node(int data)
    {
        this.data = data;
        left = null;
        right = null;
    }
}

class LCA
{
    public static void main(String[] args)
    {
        Node root = new Node(1);
        Node left = new Node(2);
        Node right = new Node(3);
        Node leftLeft = new Node(4);
        Node leftRight = new Node(5);

        root.left = left;
        root.right = right;
        left.left = leftLeft;
        left.right = leftRight;

        Node result = lca(root, 4, 5);
        System.out.println(result.data); // expect 2
    }

    static class LCAResult
    {
        boolean hasV1 = false;
        boolean hasV2 = false;
        Node lca = null;

        LCAResult(boolean hasV1, boolean hasV2, Node lca)
        {
            this.hasV1 = hasV1;
            this.hasV2 = hasV2;
            this.lca = lca;
        }

        LCAResult() {}
    }

    static LCAResult lcaHelper(Node node, int v1, int v2)
    {
        if (node.left == null && node.right == null) {
            return new LCAResult(v1 == node.data, v2 == node.data, null);
        }

        LCAResult leftResult = new LCAResult();
        LCAResult rightResult = new LCAResult();

        if (node.left != null) {
            leftResult = lcaHelper(node.left, v1, v2);
            if (leftResult.lca != null) {
                return leftResult;
            }
        }
        if (node.right != null) {
            rightResult = lcaHelper(node.right, v1, v2);
            if (rightResult.lca != null) {
                return rightResult;
            }
        }

        boolean hasV1 = leftResult.hasV1 || rightResult.hasV1 || v1 == node.data;
        boolean hasV2 = leftResult.hasV2 || rightResult.hasV2 || v2 == node.data;
        Node lca = null;

        if (hasV1 && hasV2) {
            lca = node;
        }

        return new LCAResult(hasV1, hasV2, lca);
    }

    static Node lca(Node root, int v1, int v2)
    {
        return lcaHelper(root, v1, v2).lca;
    }
}





