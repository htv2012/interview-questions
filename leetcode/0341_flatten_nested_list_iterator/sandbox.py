# sandbox.py
from solution import NestedInteger, NestedIterator

n = NestedInteger([1, 2, 3, [4, 5, [6, 7]]])
ni = NestedIterator(n)

out = []
while ni.hasNext():
    out.append(ni.next())

print(out)
