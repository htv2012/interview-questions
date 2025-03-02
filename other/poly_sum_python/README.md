@file poly_sum.md

# Sum of Polynomial

### Problem

Given two list of dictionaries representing two polynomial expressions,
write a function to add them together. Below is an example input.

	# 4x^3 + X
	p = [
	    {'co': 4, 'exp': 3},
	    {'co': 1, 'exp': 1}
	]
	
	# 3x^3 + 5x^2
	q = [
	    {'co': 3, 'exp': 3},
	    {'co': 5, 'exp': 2}
	]
	
For each expression, the list is sorted by order of decreasing exponent.
I encountered this question in an on-site interview and I did not do
well.

### First Solution

	def poly_sum(p, q):
	    a = p[:]
	    b = q[:]
	    while a and b:
	        if a[0]['exp'] > b[0]['exp']:
	            yield dict(a.pop(0))
	        elif a[0]['exp'] < b[0]['exp']:
	            yield dict(b.pop(0))
	        else:
	            dict_a = dict(a.pop(0))
	            dict_b = b.pop(0)
	            dict_a['co'] += dict_b['co']
	            yield dict_a
	    while a:
	        yield dict(a.pop(0))
	    while b:
	        yield dict(b.pop(0))
	

This solution is clunky, lengthy and not clean, but it gets the job
done. There are several areas which could see improvements:

- Three while loops
- copying the whole arrays (p==>a, q==>b)
- Lots of indexing such as a[0]['exp']

### Second solution

	import collections
	
	def poly_sum(*args):
	    psum = collections.Counter()
	    for polynomial in args:
	        for term in polynomial:
	            psum.update({term['exp']: term['co']})
	    return [{'exp':k, 'co':psum[k]} for k in sorted(psum, reverse=True)]

In this solution, I used `collections.Counter` class to keep track of
the sum of coefficients. At the end of the function, I turned the
Counter object back to the original form, which is a list of
dictionaries.

Some interviewers might not allow the use of collections module, so this
should not be your only one solution.

### Third Solution

I like the idea of the second solution, but would like to do so without
the help of the collections module: some interviewer requires *homemade*
solution, which does not rely on standard library modules.

	def poly_sum(*args):
	    psum = {}
	    for poly in args:
	        for term in poly:
	            co, exp = (term['co'], term['exp'])
	            psum.setdefault(exp, 0)
	            psum[exp] += co
	    result = [{'exp': exp, 'co': psum[exp]} for exp in sorted(psum, reverse=True)]
	    return result

This solution is almost identical to the second one, but in which I keep
track of the sum myself instead of relying on the collections module.

This solution is not perfect: the `sorted()` call does take some time,
which could be a performance hit if the dictionary `psum` is long.



