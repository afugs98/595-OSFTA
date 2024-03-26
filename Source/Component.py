class Component:
    tree_type = "Boolean"

    def __init__(self, id, fail_rate, left, right, dep_rel) -> None:
        # self.name = name
        self.id = id
        self.fail_rate = fail_rate
        # relationships: AND, OR, NOISY AND, NOISY OR
        self.dep_rel = dep_rel
        self.left = left
        self.right = right
        
    @classmethod
    def set_tree_type(cls, tree_type):
        cls.tree_type = tree_type
    
    @classmethod
    def get_tree_type(cls):
        return cls.tree_type
    
    def add_children(self, node):
        self.children.append(node)
    
    def compute_fail(self):
        pass

    def __str__(self):
        left = self.left.id if isinstance(self.left, Component) else self.left
        right = self.right.id if isinstance(self.right, Component) else self.right
        return "ID: {0}, left: {1}, right: {2}, operator: {3}".format(self.id, left, right, self.dep_rel)
        # return self.id
        # return right if right else "None"

class UnprocessedComponent (Component):
    def __init__(self, id, fail_rate, unprocessed_dep, left=None, right=None, dep_rel=None) -> None:
        super().__init__(id, fail_rate, left, right, dep_rel)
        self.unprocessed_dep = unprocessed_dep

class DummyComponent (Component):
    def __init__(self, id, fail_rate, left, right, dep_rel) -> None:
        super().__init__(id, fail_rate, left, right, dep_rel)

class RootComponent (Component):
    def __init__(self, id, fail_rate, left=None, right=None, dep_rel=None) -> None:
        super().__init__(id, fail_rate, left, right, dep_rel)





    




    
