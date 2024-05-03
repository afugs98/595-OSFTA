class Component:
    tree_type = "Boolean"

    def __init__(self, id, fail_rate, left, right, dep_rel) -> None:
        self.id = id
        self.fail_rate = fail_rate
        self.dep_rel = dep_rel
        self.left = left
        self.right = right
        
    @classmethod
    def set_tree_type(cls, tree_type):
        cls.tree_type = tree_type
    
    @classmethod
    def get_tree_type(cls):
        return cls.tree_type
    
    def compute_fail(self):
        pass

    def __str__(self):
        left = self.left.id if isinstance(self.left, Component) else self.left
        right = self.right.id if isinstance(self.right, Component) else self.right
        return "ID: {0}, left: {1}, right: {2}, operator: {3}".format(self.id, left, right, self.dep_rel)

    def get_probability(self):
        return self.fail_rate
    
    def set_probability(self, fail_rate):
        self.fail_rate = fail_rate
        return

    def get_dep_rel(self):
        return self.dep_rel

    def set_dep_rel(self, dep_rel):
        self.dep_rel = dep_rel
        return

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





    




    
