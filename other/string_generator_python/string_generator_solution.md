@file string_generator_solution.md

# String Generator

[link][1]

### Problem

Given a string (for example: "a?bc?def?g"), write a program to generate
all the possible strings by replacing ? with 0 and 1. 

Example:

Input: a?b?c?  
Output: a0b0c0, a0b0c1, a0b1c0, a0b1c1, a1b0c0, a1b0c1, a1b1c0, a1b1c1  

### Recursive Solution

Most of the solutions I from the internet employs recursion: A function replaces one question mark with either **0** or **1**, then call itself recursively to replace the rest.

### Iterative Solution

Before going into my solution, I would like to point out a couple of observations:

- Since we are replacing a question mark (?) with either digit zero or one, the solution deals with binary digits
- If we disregard all other characters in the string and concentrate on just the question marks, then we see that the problem reduces to binary number generator. For example, if we reduce the string `'a?b?c?'` to `'???'`, then the solution will be `'000'`, `'001'`, `'010'`, `'011'`, `'100'`, `'101'`, `'110'`, `'111'`.
- For a string with N question marks, there will be 2^N solutions

### The Code

	def string_generator(mystr):
	    question_mark_count = mystr.count('?')
	    possibilities = pow(2, question_mark_count)
	    for i in range(possibilities):
	        replacement = '{0:0{w}b}'.format(i, w=question_mark_count)
	        it = iter(replacement)
	        yield ''.join(c if c != '?' else next(it) for c in mystr)
	
	def main():
	    mystr = 'a?b?c?'
	    for s in string_generator(mystr):
	        print s
	
	if __name__ == '__main__':
	    main()

### Output

	a0b0c0
	a0b0c1
	a0b1c0
	a0b1c1
	a1b0c0
	a1b0c1
	a1b1c0
	a1b1c1

### Discussion

- I code my solution in Python because the language has a [generator][2] feature. However, there should be no problem implementing my solution in other languages.
- The function starts out by counting the number of question marks. If the string does not contain any question mark, then there is only one solution: the string itself.
- The next step is to calculate the number of solution or `possibilities` in the code. This is the number of strings returned by the function
- For example, if there are 3 question marks, then there are 2^3 = 8 possibilities
- Next, I loop through all the numbers from 0 to possibilities -1 (i.e. 0-7)
- For each number `i`, I turn it into a binary string, `replacement` (e.g. 5 ==> '101')
- The `yield` command loops through the string and replace the question marks with the binary digit in the replacement sequence


[1]: http://www.careercup.com/question?id=5192571630387200
[2]: https://wiki.python.org/moin/Generators



