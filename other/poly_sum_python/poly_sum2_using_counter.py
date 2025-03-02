import collections

def poly_sum(*args):
    psum = collections.Counter()
    for polynomial in args:
        for term in polynomial:
            psum.update({term['exp']: term['co']})
    return [{'exp':k, 'co':psum[k]} for k in sorted(psum, reverse=True)]

def poly_print(p, label):
    print label, '=',
    print ' + '.join('{0[co]}x^{0[exp]}'.format(t) for t in p)

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

poly_print(p, 'P')
poly_print(q, 'Q')

x = list(poly_sum(p, q))
poly_print(x, 'P + Q')