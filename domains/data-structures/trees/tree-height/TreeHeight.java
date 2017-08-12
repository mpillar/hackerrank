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

class BinaryTree {
    static int height(Node root) {
        return calculateHeightRecursive(root, 0);
    }

    private static int calculateHeightRecursive(Node current, int height)
    {
        int result = height;

        if (current.left != null) {
            result = Math.max(result, calculateHeightRecursive(current.left, height+1));
        }

        if (current.right != null) {
            result = Math.max(result, calculateHeightRecursive(current.right, height+1));
        }

        return result;
    }

    static Node insert(Node root, int data) {
        if (root == null) {
            return new Node(data);
        } else {
            Node cur;
            if (data <= root.data) {
                cur = insert(root.left, data);
                root.left = cur;
            } else {
                cur = insert(root.right, data);
                root.right = cur;
            }
            return root;
        }
    }
}

class TreeHeight
{
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int t = scan.nextInt();
        Node root = null;
        while(t-- > 0){
            int data = scan.nextInt();
            root = BinaryTree.insert(root, data);
        }
        scan.close();
        int height = BinaryTree.height(root);
        System.out.println(height);
    }
}
