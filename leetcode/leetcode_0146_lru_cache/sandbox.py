from solution import DList


def p(li: DList):
    print(f"Forward:  {[n.val for n in li]}")
    print(f"Backward: {[n.val for n in reversed(li)]}")


d = DList()
for i in range(5):
    d.prepend(i)

p(d)

# grab middle node
node = next((node for node in d if node.val == 3), None)
print(node)
