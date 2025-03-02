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
# print 'x =', x
poly_print(x, 'P + Q')