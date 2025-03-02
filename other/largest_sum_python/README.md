# Introduction
This is an interview question, which can be found in Jon Bentley's book
*Programming Pearls*.

# Problem
Given a vector x[n], compute the maximum sum found in any contiguous
subvector.

# Solution
This solution comes straight from Bentley's book, with some modification.
Bentley's solution will fail if the vector contains only negative numbers.
In such case, maximum sum is the largest element in the vector.
For example:

	[ -1, -2, -3 ] --> -1
