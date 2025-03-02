# Problem

Given a list of integers containing equal number of odd and even
numbers rearrange them in such a way that odd number is at odd
zero-based index.


# Examples

    [3, 1, 5, 2, 4, 6] ==> [2, 1, 6, 3, 4, 5]
    [1, 2, 3, 4] ==> [2, 1, 4, 3]
    [2, 3, 4, 7] ==> [2, 3, 4, 7]  # No arrangement required


# Solutions

There are several solutions to this problem, each has its pros and
cons

## Merge odd- and even lists

In this solution, we create two new empty lists, put all the odd
numbers into one and even numbers into other. We can then merge
them into a new list. We can optimize this solution a little by
merging into the original list, thus save some space. This solution
is easy to understand.

Since we only scan the list once and the merge step is also going
through the lists only once, the complexity of this methid is O(n).
This solution requires two separate lists, each half the size of
the original, which means it trades memory allocation (space) for
performance (time).

## In-place swapping

In this solution, we scan through each element of the list. If we
find an element that disagrees with its index. For example, an odd
element at an even index then we start another loop to look for the
reverse: an even element at an odd index. Once found we swap them
and exit the inner loop.

This solution has a complexity of O(n^2) because of the nested
loops. It works best for cases when the list requires little
arrangement. The worse case scenario comes when most of the odd
elements concentrate at one end of the list, which requires long
travel for the inner loop.

## Hybrid odd- and even queues

We have two queues, one to store the indices of those odd elements
that are in the wrong places and one for the even elements.  These
queue are empty initially.  We scan the list once, if we see a place
where the index and element disagrees, say an odd element at an
even index.  In this case, if the even-element queue is empty, we
cannot swap the two elements. For that, we add the index of this
odd element to the odd-element queue and move on. If the even-element
queue is not empty, we pop an index out and swap.

This method has the advantage of O(n) complexity due to scanning
the list only once. It sacrifies some space (the two queues) for
some performance gain. At the worse case scenario, all the odd
elements are at one end of the list.  In this case, the odd- or
even-element queue will grow to a quarter the size of the original
list: only half of the odd elements are out of places and the number
of odd elements take up half of the original list.


## Linear scan

In an infinite loop, first, scan to the first even index that need
swapping. Next, scan to the first odd index that need swapping. Swap
and repeat. If any index exceeds the array size, then we are done.

# How to build

The build system requires CMake 2.8.12 or later. Follow these steps:

    mkdir build
    cd build
    cmake ..                        # Create a build environment here
    make                            # Build library and test
    ./odd_event_arrangement_testst  # Run test

To clean, just remove the whole `build` directory.
