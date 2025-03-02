@file RecruitingPoint.md

# String-to-Int Conversion

### The Problem

Given a String of digits (and possibly signs) such as "123", write
a routine int stringToInteger( String s ) that converts the string
to an integer, without using the built in Java functions that would
do this. The code should handle reasonable edge and error conditions
gracefully. (You can rely on the input being in base-10 representation
- no need to worry about hex, octal, or binary input.)

### The Solution

We created a class called TypeConversion, which contains a member
function called stringToInteger(). Here are some facts about this
function:

- It can understand base-10 integers with or without sign
- It can handle values ranging from Integer.MIN_VALUE to
  Integer.MAX_VALUE
- It throws NumberFormatException for those invalid cases

### Files

- TypeConversion.java: the solution
- TypeConversionTest.java: the test suite

# Ternary Tree

### The Problem

Implement the class (or classes) required for a ternary tree. Then
implement a function that would add an element to this tree, keeping
all invariants intact.

The ternary tree is much like a binary tree but with 3 child nodes for
each parent instead of two - with the left node being values < parent,
the right node values > parent, and the middle node values == parent.
For example, if I added the following nodes to the tree in this order:
5, 4, 9, 5, 7, 2, 2 --  the tree would look like this:

                5
               /|\
              4 5 9
             /   /
             2  7
             |
             2

### The Solution

Writing code to solve the problem is the easy part. However, it is hard
to test the correctness of the solution, in this case, the insert()
method. 

Our approach is to rely on the fact that we can verify the shape of the
tree using the output of both in-order- and pre-order traversal. In our
test, we build a tree, then calls the inOrderTraversal() and 
preOrderTraversal() methods on the tree. We also created a method called
visit() which visits each node and verify the node's contents.

The problem of our approach is we are testing 3 methods at once. Hence,
when an error comes up, it could be any where within those functions,
making pin-pointing the problem much harder. On the other hand, 
traversal functions are fairly simple and straight forward to 
investigate, so that leaves us with insert().

### Files

- TernaryTree.java: The solution
- TernaryTreeConstructorTest.java: Tests for constructor
- TernaryTreeInsertAndTraversalTest.java: Tests for insert()
- TernaryTreeExample.java: A sample of how to use it
