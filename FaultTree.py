import Component
from collections import deque

class FaultTree:
    def __init__(self, head: Component=None) -> None:
        # design choices: should we create the head component when initializing fault tree object?
        self.head = head

    def print_tree(self):
        queue = deque([self.head])
        while queue:
            node = queue.popleft()
            print("Name:", node.name, "| ID:", node.id, "| Fail Rate:", node.fail_rate)
            for child in node.children:
                queue.append(child)
                






    