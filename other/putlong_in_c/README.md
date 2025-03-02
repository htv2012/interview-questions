# Problem

Write a function `putlong` which takes a long integer as parameter
and write that number to the standard output.  The function only
use `putchar` as its means to write a character to the standard
output.  The function should not use any data structures such as
array, stack, queue... to store the digits.

Things to watch for:

- Edge cases such as: 0, -1, numbers near and at LONG_MAX, LONG_MIN,
  numbers which ends with zero
- Divide by zero error
- Overflow, underflow
- Negative number handling

# Follow-up questions

- Walk through a couple of examples
- How does it work against edge cases
- How to test it
- Any improvement?

# Strategy

If allowed to use a stack, I would keep divide the number by 10 and
push the remainder to a stack until the number becomes zero. Next,
just pop the stack one by one and write to the standard output.
Since the question prohibits the use of data structures such as
stack to store the digits, I have to come up with a different
strategy.

In order to extract the digits from left to right from a long
integer, I will have to divide it with a multiple of 1 (1, 10, 100,
etc.). For example, given the number 975:

- Divide 975 by 100 and get 9, remainder is 75, print 9
- Divide 75 by 10 and get 7, remainder is 5, print 7
- Divide 5 by 1 and get 5, remainder is 0, print 5
