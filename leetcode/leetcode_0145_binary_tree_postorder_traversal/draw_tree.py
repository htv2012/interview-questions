from graphviz import Digraph


# 2. Define the drawing helper function
def draw_tree(root):
    if not root:
        return "Empty Tree"

    dot = Digraph()
    # Use circle shape for a clean look
    dot.attr("node", shape="circle")

    def add_nodes_edges(node):
        # Create a unique ID for the node using its memory address
        node_id = str(id(node))
        dot.node(node_id, label=str(node.val))

        if node.left:
            left_id = str(id(node.left))
            dot.edge(node_id, left_id)
            add_nodes_edges(node.left)

        if node.right:
            right_id = str(id(node.right))
            dot.edge(node_id, right_id)
            add_nodes_edges(node.right)

    add_nodes_edges(root)
    return dot
