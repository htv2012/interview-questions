def poly_sum(*args):
    psum = {}
    for poly in args:
        for term in poly:
            co, exp = (term['co'], term['exp'])
            psum.setdefault(exp, 0)
            psum[exp] += co
    result = [{'exp': exp, 'co': psum[exp]} for exp in sorted(psum, reverse=True)]
    return result

def poly_print(p, label):
    print label, '=',
    print ' + '.join('{0[co]}x^{0[exp]}'.format(t) for t in p)

# Main

p = [
    {'co': 10, 'exp': 4},
    {'co': 4, 'exp': 3},
    {'co': 1, 'exp': 1}
]

q = [
    {'co': 2, 'exp': 5},
    {'co': 3, 'exp': 3},
    {'co': 5, 'exp': 2}
]

poly_print(p, 'P')
poly_print(q, 'Q')

x = list(poly_sum(p, q))
# print 'x =', x
poly_print(x, 'S')