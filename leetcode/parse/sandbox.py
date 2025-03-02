# sandbox.py
import ast

with open("solution0897.txt") as stream:
    text = stream.read().strip() + "\n        pass"

mod = ast.parse(text)

# Search for the "Solution" class
sol = next(
    (
        obj
        for obj in ast.iter_child_nodes(mod)
        if isinstance(obj, ast.ClassDef) and obj.name == "Solution"
    ),
    None,
)
print(ast.unparse(sol))
