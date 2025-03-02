#ifndef LIST_H_56F7B
#define LIST_H_56F7B
/**
 * @file List.h
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
 * A linked list implementation
 */
class List {
public:
    class Node {
    public:
        Node();
        Node(int new_data, Node *next_node=NULL);
    public:
        int data;
        Node *next;
    };

    class iterator: 
        public std::iterator<std::forward_iterator_tag, int> {
    public:
        iterator(): _node(NULL) {}
        iterator(Node* p): _node(p) {}

        iterator& operator=(const iterator& other);
        bool operator==(const iterator& other);
        bool operator!=(const iterator& other);
        iterator& operator++();
        iterator& operator++(int);
        int operator*();
    private:
        Node* _node;
    };

    /** 
     * Returns an iterator pointing to the first element. The caller
     * must not dereference the iterator if the list is empty, or if
     * the iterator is equal to end().
     */
    iterator begin() { return iterator(_head); }

    /** 
     * Returns an iterator pointing pass the last element. The caller
     * must not to dereference the iterator once it reaches end().
     */
    iterator end()   { return iterator(NULL); }

    /**
     * Create a new, empty list.
     */
    List();

    /**
     * Clean up the storage space which the list allocated.
     */
    ~List();

    /**
     * Adds a new value to the end of the list.
     * @param value Value to be duplicated to the new element.
     */
    void push_back(const int& value);


    /**
     * Calculates the number of elements (size) in the list.
     * @return The size of the list, 0 for empty list.
     */
    unsigned int size();

    /**
     * Determines if a list is empty (having no element) or not.
     * @return  True if the list is empty, false otherwise.
     */
    bool empty();

    Node* get_head();
    Node* get_tail();

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
    bool has_loop();

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
    void reverse();
    
private:
    Node *_head;
    Node *_tail;
    unsigned int _size;
};

#endif // LIST_H_56F7B

