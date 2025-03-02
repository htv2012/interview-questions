#!/usr/bin/env python

"""
@file intersection.py
@author Hai Vu
"""

def intersection_original(list1, list2, list3):
    """
    Given three lists, return a list of those elements that appears in
    all three.

    @param list1 The first list
    @param list2 The second list
    @param list3 The third list

    This was the solution I gave the interviewer. Given my anxiety, it
    is not a great solution.

    ### Pros:
    - Correct output
    - Scans each list only once
    - Set look up is in order O(1), very fast

    ### Cons:
    - Uses 3 separate sets
    - Not very elegant
    """ 

    set1 = set(list1)
    set2 = set()
    for i in list2:
        if i in set1:
            set2.add(i)

    set3 = set()
    result = []
    for i in list3:
        if i in set2:
            if i not in set3:
                result.append(i)
            set3.add(i)

    return result

def intersection2(list1, list2, list3):
    """
    Given three lists, return a list of those elements that appears in
    all three.

    @param list1 The first list
    @param list2 The second list
    @param list3 The third list

    After the interview, I had time to think for throughoutly, so I came
    up with this improved solution.

    ### Pros:
    - All the pros from the first solution, plus:
    - Built the first two sets quickly

    ### Cons:
    - Still requires 3 sets
    """ 

    list_intersection = set(list3) & set(list2)
    result = []
    dup = set()
    for i in list1:
        if i in list_intersection:
            if i not in dup:
                result.append(i)
            dup.add(i)
    return result

def intersection3(list1, list2, list3):
    """
    Given three lists, return a list of those elements that appears in
    all three.

    @param list1 The first list
    @param list2 The second list
    @param list3 The third list

    Unlike solution #2, this solution only uses 1 set. Keep in mind that
    all solutions create two temporary sets `set(list1)` and 
    `set(list2)`.
    """

    list_intersection = set(list1) & set(list2)
    result = []
    for i in list3:
        if i in list_intersection:
            result.append(i)
            list_intersection.remove(i)
    return result


intersection = intersection3 # uses this solution

list1 = [1,2,3,4,1,2,3,4,1,2,1,3]
list2 = [2,3,4,5,2,3,4,5,4,5]
list3 = [3,4,5,6,7,8,7,8,3]
print intersection(
        list1,
        list2,
        list3)
