# sandbox.py
from tree import breadth_first_build

from solution import get_shape

root = breadth_first_build([1, 2, 2, 2, None, 2])
left = get_shape(root.left)
print(left)

right = get_shape(root.right, is_mirror=True)
print(right)
