from collections import deque
from Source.Component import DummyComponent

class FaultTree:
    def __init__(self, root) -> None:
        self.root = root

    def print_tree(self, node, level=0):
        if not node:
            return
        indent = '  ' * level
        print(f"{indent}-> {node.id} Fail Rate: {node.get_probability()}")
    
        self.print_tree(node.left, level + 1)
        self.print_tree(node.right, level + 1)






    