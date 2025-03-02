/**
 * @file TernaryTreeInsertAndTraversalTest.java
 * Interview Coding for Recruiting Point
 * 2014-06-10
 * @author Hai Vu
 */


package net.southeastwind.haivu;

import java.util.Arrays;
import java.util.Collection;

import org.junit.Test;
import org.junit.runners.Parameterized;
import org.junit.runner.RunWith;
import static org.junit.Assert.*;

/**
 * Tests for TernaryTree's insert(). We can test it by insert, then
 * verify that the tree is in a particular shape. The tricky part is to
 * verify the shape of the tree. One way to do so is to look at the
 * output of inOrderTraversal() and preOrderTraversal().
 * @author Hai Vu
 */
@RunWith(Parameterized.class)
public class TernaryTreeInsertAndTraversalTest implements TernaryTree.NodeVisitor {
    private final Integer[] inputList;
    private final Integer[] expectedInOrder;
    private final Integer[] expectedPreOrder;
    private TernaryTree t;

    /**
     * Constructor to transfer test data 
     * @param inList The input. A list of integers to insert into the tree.
     * @param outputInOrder Expected output of inOrderTraversal(), used for verification.
     * @param outputPreOrder Expected output of preOrderTraversal(), used for verification.
     */
    public TernaryTreeInsertAndTraversalTest(
            Integer[] inList, 
            Integer[] outputInOrder, 
            Integer[] outputPreOrder) {
        
        this.inputList = inList;
        this.expectedInOrder = outputInOrder;
        this.expectedPreOrder = outputPreOrder;
    }

    /**
     * Test parameters. The return value is a list of 3 sublist:
     * - The input
     * - The expected inOrderTraversal() order
     * - The expected preOrderTraversal() order
     * @return List of test cases.
     */
    @Parameterized.Parameters
    public static Collection testCases() {
        return Arrays.asList(new Integer[][][] {
            // A simple, single node
            { {5}, {5}, {5} },
            
            // Two nodes
            { {5, 4}, {4, 5}, {5, 4} },
            { {5, 9}, {5, 9}, {5, 9} },
            
            // More complex test cases
            { {5, 4, 9}, {4, 5, 9}, {5, 4, 9} },
            { {5,4,9,5,7,2,2,4,3,10,8,9}, {2,2,3,4,4,5,5,7,8,9,9,10}, {5,4,2,2,3,4,5,9,7,8,9,10} }
        });
    }

    /**
     * Visits each node in a tree and verify its data. Since we are allowed only
     * one "visit" function per class. This function checks both the in-order
     * and pre-order traversal. It uses two data members: index to know which
     * slot in the expected* array to check for, and checkType to know which 
     * array it should use for verification.
     * @param t 
     */
    @Override
    public void visit(TernaryTree t) {
        if (this.CheckType == CheckType.IN_ORDER) {
            assertEquals(
                    String.format("In-order check at index [%d]", index),
                    this.expectedInOrder[index], 
                    t.getData());
        } else if (this.CheckType == CheckType.PRE_ORDER) {
            assertEquals(
                    String.format("Pre-order check at index [%d]", index),
                    this.expectedPreOrder[index], 
                    t.getData());
        }
        ++index; // Advance to the next check point for next time
    }
    
    /**
     * Sets which position in the expected* array the visit() function should
     * use to verify the tree.
     */
    private Integer index;
    
    /**
     * Specifies which array to verify against: expectedInOrder or 
     * expectedPreOrder.
     */
    private enum CheckType { IN_ORDER, PRE_ORDER };
    
    /**
     * Specifies which array to verify against: expectedInOrder or 
     * expectedPreOrder.
     */
    private CheckType CheckType;

    /**
     * Perform a test against a set of data: First, the function inserts a list
     * of integers into the tree. It then verifies the correctness by traversing
     * the tree in in-order and pre-order manners. Each time, the visit() 
     * function will be call upon to verify the contents of each node in the 
     * tree.
     */
    @Test
    public void testUsingTraversal() {
        
        // Insert the nodes 
        for (Integer nodeData: this.inputList) {
            TernaryTree node = new TernaryTree(nodeData);
            if (t == null) {
                t = node;
            } else {
                t.insert(node);
            }
        }
        
        // Check using InOrderTraversal
        this.index = 0;
        this.CheckType = CheckType.IN_ORDER;
        t.inOrderTraversal(this);
        
        // Check using PreOrderTraversal
        this.index = 0;
        this.CheckType = CheckType.PRE_ORDER;
        t.preOrderTraversal(this);
    }

}
