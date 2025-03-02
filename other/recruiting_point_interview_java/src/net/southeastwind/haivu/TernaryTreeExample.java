package net.southeastwind.haivu;

/**
 * @file TernaryTreeExample.java
 * This is an example of how one might use the TernaryTree class. It
 * demonstrates the following methods:
 * 
 * - TernaryTree() (constructor)
 * - insert()
 * - inOrderTraversal()
 * - preOrderTraversal()
 * 
 * In this example, we insert the following nodes in order: 5, 4, 9, 5, 7, 2, 2, 4, 3, 10, 8, 9
 * 
 * The tree will look like this:
 *
 *                           5  
 *                         / | \  
 *                        /  5  \  
 *                       4       9  
 *                      /|      /|\  
 *                     2 4     7 9 10  
 *                     |\        \  
 *                     2 3        8  
 */

/**
 *
 * @author Hai Vu
 */
public class TernaryTreeExample implements TernaryTree.NodeVisitor {

    @Override
    public void visit(TernaryTree t) {
        System.out.printf("%d ", t.getData());
    }
    
    /**
     * An example to try out some features of the TernaryTree class.
     */
    public void example() {
        System.out.println("TernaryTree Example");
        TernaryTree t = new TernaryTree(5); // Root node
        Integer[] values = {4, 9, 5, 7, 2, 2, 4, 3, 10, 8, 9};
        
        for (Integer data: values) {
            t.insert(new TernaryTree(data));
        }
        
        System.out.print("\nIn order traversal:   ");
        t.inOrderTraversal(this);
        System.out.print("\nPre order traversal:  ");
        t.preOrderTraversal(this);
        System.out.println("");
    }
    
    public static void main(String[] args) {
        TernaryTreeExample tte = new TernaryTreeExample();
        tte.example();
    }
    
}
