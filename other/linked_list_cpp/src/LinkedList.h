#pragma once
/**
 * @file LinkedList.h
 *
 * A collection of linked list interview questions.
 *
 * - Loop detection in has_loop.cpp
 * - Reverse a linked list in reverse.cpp
 *
 */

#include <cstdlib>
#include <iterator>

/**
 * A node in a linked list
 */
template <class T>
class Node {
public:
    Node<T>();
    Node<T>(T new_data, Node *next_node=nullptr);
public:
    T data;
    Node<T> *next;
};

/**
 * Iterator through the nodes
 */
template <class T>
class iterator:
    public std::iterator<std::forward_iterator_tag, int> {
public:
    iterator(): _node(nullptr) {}
    iterator(Node<T>& p): _node(p) {}

    iterator& operator=(const iterator& other);
    bool operator==(const iterator& other);
    bool operator!=(const iterator& other);
    iterator& operator++();
    iterator& operator++(int);
    T operator*();
private:
    Node<T>* _node;
};


/**
 * A linked list implementation
 */
template <class T>
class LinkedList {
public:

    /**
     * Returns an iterator pointing to the first element. The caller
     * must not dereference the iterator if the list is empty, or if
     * the iterator is equal to end().
     */
    // iterator begin() { return iterator(_head); }

    /**
     * Returns an iterator pointing pass the last element. The caller
     * must not to dereference the iterator once it reaches end().
     */
    // iterator end()   { return iterator(nullptr); }

    /**
     * Create a new, empty list.
     */
    LinkedList<T>(): _head(), _tail(), _size(0) {}

    /**
     * Clean up the storage space which the list allocated.
     */
    ~LinkedList<T>() {}

    /**
     * Adds a new value to the end of the list.
     * @param value Value to be duplicated to the new element.
     */
    void push_back(const T& value);


    /**
     * Calculates the number of elements (size) in the list.
     * @return The size of the list, 0 for empty list.
     */
    unsigned int size() { return _size; }

    /**
     * Determines if a list is empty (having no element) or not.
     * @return  True if the list is empty, false otherwise.
     */
    // bool empty();

    Node<T>* get_head() { return _head; }
    Node<T>* get_tail() { return _tail; }

    /*******************************************************************
     * Interview Questions
     ******************************************************************/

    /**
    Given a singly linked list, determine if the list has loop (cycle).

    #### References

    - [Cycle detection algorithm]
      (http://en.wikipedia.org/wiki/Cycle_detection)
    - [Brent's algorithm](http://www.siafoo.net/algorithm/11)
    */
    // bool has_loop();

     /**
      *
      * Given a singly linked list, write code to reverse that list.
      *
      * #### Restrictions
      *
      * - Not to use recursive algorithm
      * - Do not allocate memory to hold all the list elements
      *
      * #### Stragegy
      *
      * My solution is to use three pointers: `previous`, `current`, and
      * `next`. These three pointers points to successive nodes. As I move
      * forward, I fixed the `->next` pointer for each node until reaching
      * the end of the list.
      *
      * #### Discussion
      *
      * This is one way to reverse a linked list. Another way is to use
      * recursion. In general, I prefer the non-recursion solution.
      */
    // void reverse();

private:
    Node<T> *_head;
    Node<T> *_tail;
    unsigned int _size;
};
