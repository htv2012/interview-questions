# sandbox.py
from tree import breadth_first_build

from solution import all_paths

root = breadth_first_build(range(1, 8))
for s in all_paths(root):
    print(s)
