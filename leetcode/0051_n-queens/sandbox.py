import string

from solution import Board

fill = string.printable
size = 9
assert len(fill) > size * size

b = Board(size)
for coord, c in zip(b, fill):
    b[coord] = c
print(b)

row_index = 1
col_index = 2

print(f"Reach of {row_index=}, {col_index=}, {b[row_index, col_index]=}")
for c in b.reach(row_index, col_index):
    print(c, end=" ")
print()
