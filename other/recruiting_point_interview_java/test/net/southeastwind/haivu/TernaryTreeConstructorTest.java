/**
 * @file TernaryTreeConstructorTest.java
 * Interview Coding for Recruiting Point
 * 2014-06-10
 * @author Hai Vu
 */

package net.southeastwind.haivu;

import org.junit.Before;
import org.junit.Test;
import static org.junit.Assert.*;

/**
 * A simple set of tests to verify that the constructor does its job.
 * @author Hai Vu
 */
public class TernaryTreeConstructorTest {
    
    private TernaryTree t;
    private Integer data;

    /**
     * Constructs a new node so the tests can verify the node's integrity.
     */
    @Before
    public void setUp() {
        data = 5;
        t = new TernaryTree(data);
    }

    /**
     * Verifies that the tree (single node) is not null after created. We
     * assume the system has enough memory to create the node.
     */
    @Test public void testNotNull()      { assertNotNull(t); }
    
    /**
     * Verifies the data is what we put in when we created the tree.
     */
    @Test public void testData()         { assertEquals(data, t.getData()); }
    
    /**
     * Verifies the left branch of the node is null when it is created
     */
    @Test public void testLeftBranch()   { assertNull(t.left); }
    
    /**
     * Verifies the middle branch of the node is null when it is created
     */
    @Test public void testMiddleBranch() { assertNull(t.middle); }
    
    /**
     * Verifies the right branch of the node is null when it is created
     */
    @Test public void testRightBranch()  { assertNull(t.right); }
}
