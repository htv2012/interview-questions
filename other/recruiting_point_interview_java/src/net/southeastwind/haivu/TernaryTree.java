/**
 * @file TernaryTree.java
 * Interview Coding for Recruiting Point
 * 2014-06-10
 * @author Hai Vu
 */


package net.southeastwind.haivu;

/**
 * Implement the class (or classes) required for a ternary tree. Then
 * implement a function that would add an element to this tree, keeping
 * all invariants intact.
 * 
 * The ternary tree is much like a binary tree but with 3 child nodes
 * for each parent instead of two - with the left node being values <
 * parent, the right node values > parent, and the middle node values ==
 * parent.  For example, if I added the following nodes to the tree in
 * this order: 5, 4, 9, 5, 7, 2, 2 --  the tree would look like this:
 * 
 *                 5
 *                /|\
 *               4 5 9
 *              /   /
 *              2  7
 *              |
 *              2
 */

public class TernaryTree {

    //** The value contain in the node */
    private Integer data;        

    /** Points to the nodes with smaller values */
    public TernaryTree left;   

    /** Points to the nodes with same values */
    public TernaryTree middle; 

    /** Points to the nodes with larger values */
    public TernaryTree right;  
    
    /**
     * Construct a new tree with a single node.
     * @param nodeData The data contain in the node
     */
    public TernaryTree(int nodeData) {
        this.data = nodeData;
        this.left = null;
        this.middle = null;
        this.right = null;        
    }

    /**
     * Returns the data contain in the tree's node.
     * @return An integer representing the node's data.
     */
    public Integer getData() { return this.data; }

    /**
     * Inserts a new node into the current tree. Nodes with smaller 
     * values will be inserted to the left trees. Nodes with larger 
     * values will be inserted to the right tree. Nodes with equal 
     * values will be inserted to the middle tree.
     * @param t The new node to be inserted.
     */
    public void insert(TernaryTree t) {
        TernaryTree branch = this;
        while (branch != null) {
            TernaryTree parent = branch;
            if (t.getData() < branch.getData()) {
                branch = branch.left;
                if (branch == null) { parent.left = t; }
            } else if (t.getData() > branch.getData()) {
                branch = branch.right;            
                if (branch == null) { parent.right = t; }    
            } else {
                branch = branch.middle;
                if (branch == null) { parent.middle = t; }
            }
        }
    }

    /**
     * An interface for traversal. A class can implement this interface
     * and call one of the *Traversal() methods, passing in an 
     * implementation of this interface. The *Traversal() methods will
     * call the visit() method at each node.
     */
    public interface NodeVisitor {
        /**
         * A function to visit each node. When passed in one of the 
         * *Traversal() functions, the visit method will be called for
         * each node visited. One example of this function is to print
         * out the contents of the node.
         * @see TernaryTreeExample.java
         * @param t The node visited.
         */
        public void visit(TernaryTree t);
    }

    /**
     * Traverse the tree in in-order manner. The result will be sorted 
     * in ascending order.
     * @param visitor The implementation of the NodeVisitor interface. 
     * At each node, the visit() method will be called to process the 
     * node.
     */
    public void inOrderTraversal(NodeVisitor visitor) {
        if (this.left != null)   { this.left.inOrderTraversal(visitor); }
        visitor.visit(this);
        if (this.middle != null) { this.middle.inOrderTraversal(visitor); }
        if (this.right != null)  { this.right.inOrderTraversal(visitor); }
    }
    
    /**
     * Traverse the tree in pre-order manner. The result will be sorted in 
     * ascending order.
     * @param visitor The implementation of the NodeVisitor interface. At each
     * node, the visit() method will be called to process the node.
     */
    public void preOrderTraversal(NodeVisitor visitor) {
        visitor.visit(this);
        if (this.left != null)   { this.left.preOrderTraversal(visitor); }
        if (this.middle != null) { this.middle.preOrderTraversal(visitor); }
        if (this.right != null)  { this.right.preOrderTraversal(visitor); }
    }

}

