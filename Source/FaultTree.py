import Component
from collections import deque
from Component import DummyComponent

class FaultTree:
    def __init__(self, root) -> None:
        self.root = root

    def print_tree(self):
            
        queue = deque([self.root])
        child_q = deque()
        while queue or child_q:
            if child_q:
                node = child_q.popleft()
            else:
                node = queue.popleft()
            print("ID:", node.id)
            if type(node) is DummyComponent:
                print(node)
            if node.left:
                child_q.append(node.left)
            if node.right:
                child_q.append(node.right)
                






    