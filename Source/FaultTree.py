import Component
from collections import deque

class FaultTree:
    def __init__(self, children=[]) -> None:
        self.children = children

    def print_tree(self):
        print("Root Subcomponents: ")
        for sub in self.children:
            print(sub.id)
            
        queue = deque(self.children)
        child_q = deque()
        while queue or child_q:
            if child_q:
                node = child_q.popleft()
            else:
                node = queue.popleft()
            print("ID:", node.id)
            if node.left:
                child_q.append(node.left)
            if node.right:
                child_q.append(node.right)
                






    